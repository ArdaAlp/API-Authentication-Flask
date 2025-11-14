[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1.2-3BABC3?logo=flask&logoColor=white)](https://flask.palletsprojects.com/en/stable/)
[![SQLite](https://img.shields.io/badge/SQLite-3-003B57?logo=sqlite&logoColor=white)](https://www.sqlite.org/index.html)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-663399?logo=css&logoColor=white)

# Flask Authentication System 🔐

> 🇹🇷 **Türkçe açıklama aşağıda bulunmaktadır** | Turkish description below
> 
> 🇬🇧 **English description follows** | İngilizce açıklama devam etmektedir

## Türkçe Açıklama 🇹🇷

Flask kullanılarak geliştirilmiş modern bir kimlik doğrulama sistemi. Kullanıcı kaydı, giriş, şifre sıfırlama işlevselliği ve temiz bir kontrol paneli arayüzü içerir.

### Özellikler 🌟

- E-posta Doğrulamalı Kullanıcı Kaydı
- Güvenli Giriş Sistemi
- Şifre Sıfırlama İşlevselliği
- Kullanıcı Kontrol Paneli
- Profil Yönetimi
- Duyarlı (Responsive) Tasarım
- Temiz ve Modern Kullanıcı Arayüzü

### Kurulum 📥

1. Depoyu klonlayın
```bash
git clone https://github.com/ArdaAlp/API-Authentication-Flask.git
```

2. Sanal ortam oluşturun
```bash
python -m venv venv
```

3. Sanal ortamı etkinleştirin
```bash
# Windows
.\venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

4. Bağımlılıkları yükleyin
```bash
pip install -r requirements.txt
```

5. Uygulamayı çalıştırın
```bash
flask run
```

Uygulama `http://localhost:5000` adresinde çalışacaktır

### Kullanım 💻

1. E-posta adresinizle yeni bir hesap oluşturun
2. E-posta adresinizi doğrulayın
3. Kontrol paneline erişmek için giriş yapın
4. Profilinizi ve ayarlarınızı yönetin
5. Gerekirse şifre sıfırlama özelliğini kullanın

### Katkıda Bulunma 🤝

Katkılarınızı bekliyoruz! Lütfen Pull Request göndermekten çekinmeyin.

1. Depoyu fork edin
2. Özellik dalınızı oluşturun (`git checkout -b feature/HarikaBirOzellik`)
3. Değişikliklerinizi commit edin (`git commit -m 'Harika bir özellik ekle'`)
4. Dalınızı push edin (`git push origin feature/HarikaBirOzellik`)
5. Bir Pull Request açın

### Notlar 🔧
- *Bu proje prototipleme amacıyla hazırlanmıştır ve şifreler düz metin olarak saklanmaktadır. Üretim ortamında şifreleme kullanılmalıdır.*

- ***Projeyi geliştirmek için**, kullanıcı rolleri, token tabanlı kimlik doğrulama ekleyebilir veya bir frontend framework'ü entegre edebilirsiniz.*

- *Proje dili Türkçe'dir ve yeni dil desteği **yakında gelecek...***

---

## English Description 🇬🇧

A modern authentication system built with Flask, featuring user registration, login, password reset functionality, and a clean dashboard interface.

## Features 🌟

- User Registration with Email Verification
- Secure Login System
- Password Reset Functionality
- User Dashboard
- Profile Management
- Responsive Design
- Clean and Modern UI

## Project Structure 📂

```
├── app.py                 # Main application file
├── static/               
│   └── css/               # CSS stylesheets
│       ├── base.css
│       ├── dashboard.css
│       ├── forgotten.css
│       ├── index.css
│       ├── login.css
│       ├── profile.css
│       └── signup.css
└── templates/             # HTML templates
    ├── base.html
    ├── dashboard.html
    ├── forgotten.html
    ├── index.html
    ├── login.html
    ├── profile.html
    ├── reset_password.html
    └── signup.html
```

## Installation 📥

1. Clone the repository
```bash
git clone https://github.com/ArdaAlp/API-Authentication-Flask.git
```

2. Create a virtual environment
```bash
python -m venv venv
```

3. Activate the virtual environment
```bash
# Windows
.\venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

4. Install dependencies
```bash
pip install -r requirements.txt
```

5. Run the application
```bash
flask run
```

The application will be available at `http://localhost:5000`

## Usage 💻

1. Register a new account using your email
2. Verify your email address
3. Log in to access the dashboard
4. Manage your profile and settings
5. Use the password reset feature if needed

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Notes 🔧
- *This project is for prototyping purposes, and passwords are stored as plain text. Hashing should be used in a production environment.*

- ***To enhance the project**, you could add user roles, token-based authentication, or integrate a frontend framework.*

- *The project language is Turkish and new language support **coming soon...***
