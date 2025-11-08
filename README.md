[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1.2-3BABC3?logo=flask&logoColor=white)](https://flask.palletsprojects.com/en/stable/)
[![SQLite](https://img.shields.io/badge/SQLite-3-003B57?logo=sqlite&logoColor=white)](https://www.sqlite.org/index.html)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-663399?logo=css&logoColor=white)

# Flask Authentication System 🔐

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
