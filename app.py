from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import uuid

conn = sqlite3.connect('users.db', check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
''')

app = Flask(__name__)

app.secret_key = str(uuid.uuid4().hex)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/meltem')
def meltem():
    return "Hoş Geldin Karıcım <3"


@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        match_password = request.form['confirmPassword']

        cursor.execute('SELECT * FROM user WHERE username = ?', (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            flash('Kullanıcı adı zaten alınmış!', 'error')
            return redirect(url_for('sign_up'))

        else:
            if password != match_password:
                flash('Şifreler uyuşmuyor!', 'error')
                return redirect(url_for('sign_up'))

            else:
                cursor.execute(
                    'INSERT INTO user (username, password) VALUES (?, ?)', (username, password))
                conn.commit()
                flash('Kayıt başarılı! Giriş yapabilirsiniz.', 'success')
                return redirect(url_for('login'))

    else:
        return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        cursor.execute(
            'SELECT * FROM user WHERE username = ? AND password = ?', (username, password))
        user = cursor.fetchone()

        if user:
            session['username'] = username
            return redirect(url_for('dashboard'))

        else:
            flash('Geçersiz kullanıcı adı veya şifre!', 'error')
            return redirect(url_for('login'))

    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    if request.method == 'POST':
        new_password = request.form['newPassword']
        confirm_password = request.form['confirmPassword']
        username = session['username']

        if new_password != confirm_password:
            flash('Şifreler uyuşmuyor!', 'error')
            return render_template('reset_password.html')

        else:
            cursor.execute(
                'UPDATE user SET password = ? WHERE username = ?', (new_password, username))
            conn.commit()

            flash('Şifre başarıyla sıfırlandı!', 'success')
            session.clear()
            return redirect(url_for('login'))

    else:
        return render_template('reset_password.html')


@app.route('/forgotten', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        username = request.form['username']

        cursor.execute('SELECT * FROM user WHERE username = ?', (username,))
        user = cursor.fetchone()

        if user:
            session['username'] = username
            return redirect(url_for('reset_password'))

        else:
            flash('Kullanıcı bulunamadı!', 'error')
            return render_template('forgotten.html')

    else:
        return render_template('forgotten.html')


@app.route('/profile')
def profile():

    if 'username' not in session:
        flash('Lütfen önce giriş yapın.', 'error')
        return redirect(url_for('login'))

    else:
        username = session.get('username')
        return render_template('profile.html', username=username)


@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        flash('Lütfen önce giriş yapın.', 'error')
        return redirect(url_for('login'))

    else:
        username = session.get('username')

        cursor.execute('SELECT * FROM user WHERE username = ?', (username,))
        user_information = cursor.fetchone()

        return render_template('dashboard.html', username=user_information[1], users=user_information)


@app.route('/change_password', methods=['POST'])
def change_password():

    username = session['username']
    current_password = request.form['currentPassword']
    db_password = conn.execute(
        'SELECT password FROM user WHERE username = ?', (username,)).fetchone()[0]

    if db_password != current_password:
        flash('Mevcut Şifre Hatalı!', 'error')
        return redirect(url_for('profile'))

    elif current_password == request.form['newPassword']:
        flash('Yeni Şifre Mevcut Şifre ile Aynı Olamaz!', 'error')
        return redirect(url_for('profile'))

    else:
        new_password = request.form['newPassword']
        confirm_password = request.form['confirmPassword']

        if new_password != confirm_password:
            flash('Yeni Şifreler Uyuşmuyor!', 'error')
            return redirect(url_for('profile'))

        else:
            conn.execute(
                'UPDATE user SET password = ? WHERE username = ?', (new_password, username))
            conn.commit()

            flash('Şifre Başarıyla Değiştirildi!', 'success')
            return redirect(url_for('profile'))
