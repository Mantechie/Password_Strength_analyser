# 🔐 Password Strength Analyzer

<div align="center">

<img src="https://readme-typing-svg.herokuapp.com?font=Poppins&size=32&pause=1000&color=8A2BE2&center=true&vCenter=true&width=950&lines=Advanced+Password+Strength+Analyzer;Secure+Flask-Based+Security+Tool;Cybersecurity+%7C+Flask+%7C+SQLite+%7C+bcrypt;Real-Time+Password+Security+Analysis" />

<br>

<img src="https://img.shields.io/github/stars/Mantechie/Password_Strength_Analyser?style=for-the-badge&color=8A2BE2" />
<img src="https://img.shields.io/github/forks/Mantechie/Password_Strength_Analyser?style=for-the-badge&color=blue" />
<img src="https://img.shields.io/github/repo-size/Mantechie/Password_Strength_Analyser?style=for-the-badge&color=orange" />
<img src="https://img.shields.io/github/license/Mantechie/Password_Strength_Analyser?style=for-the-badge&color=green" />

<br><br>

<img src="https://komarev.com/ghpvc/?username=Mantechie&label=Visitors&color=8A2BE2&style=for-the-badge" />

</div>

---

# 🚀 About The Project

Password Strength Analyzer is a secure Flask-based cybersecurity application designed to evaluate password security using advanced password analysis techniques.

The project helps users understand password vulnerabilities by analyzing:

✨ Password strength  
✨ Entropy calculation  
✨ Common password usage  
✨ Sequential & repeated patterns  
✨ Password reuse detection  
✨ Secure password generation  

This project demonstrates practical implementation of cybersecurity concepts, backend security mechanisms, API development, and secure authentication workflows.

---

# 🌟 Core Features

## 🔍 Password Security Analysis

- Real-time password strength evaluation
- Entropy-based security scoring
- Common password blacklist detection
- Sequential pattern identification
- Repeated character analysis
- Password complexity validation

## 🔐 Security Features

- bcrypt password hashing
- Password reuse prevention
- Secure API validation
- Input sanitization
- XSS protection
- Secure HTTP headers
- Rate limiting implementation

## ⚡ Backend Functionality

- RESTful API architecture
- SQLite database integration
- Structured Flask backend
- Modular application design
- Middleware-based security handling

## 🧪 Testing & Reliability

- Automated testing with pytest
- Error handling & validation
- Secure production-ready architecture
- Logging & debugging workflows

---

# 🛠️ Tech Stack

<div align="center">

## 💻 Backend Technologies

<img src="https://skillicons.dev/icons?i=python,flask,sqlite" />

## 🔐 Security Tools

<img src="https://skillicons.dev/icons?i=docker,git,github" />

## 🌐 Frontend Technologies

<img src="https://skillicons.dev/icons?i=html,css,js" />

</div>

---

# 🧠 Cybersecurity Concepts Implemented

✅ Password Entropy Calculation  
✅ bcrypt Hashing Mechanism  
✅ Common Password Detection  
✅ Password Reuse Prevention  
✅ API Security Hardening  
✅ Rate Limiting Protection  
✅ Secure Input Sanitization  
✅ Secure HTTP Security Headers  
✅ XSS Mitigation Techniques  

---

# 📂 Project Structure

```bash
Password_Strength_Analyser/
│
├── app/
│   ├── api/
│   ├── middleware/
│   ├── models/
│   ├── services/
│   ├── utils/
│   ├── templates/
│   └── static/
│
├── tests/
├── requirements.txt
├── run.py
├── DOCKERFILE
└── README.md
```

---

# 🌐 API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/api/v1/health` | GET | API health check |
| `/api/v1/analyze` | POST | Analyze password strength |
| `/api/v1/generate-password` | GET | Generate secure password |
| `/api/v1/verify-password` | POST | Verify hashed password |
| `/api/v1/history` | GET | Retrieve password history |

---

# ⚙️ Installation & Setup

## 📥 Clone The Repository

```bash
git clone https://github.com/Mantechie/Password_Strength_Analyser.git
```

## 📂 Navigate Into The Project

```bash
cd Password_Strength_Analyser
```

---

# 🚀 Local Development Setup

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run The Flask Server

```bash
python run.py
```

Application runs on:

```bash
http://localhost:5000
```

---

# 🔐 Environment Configuration

Create a `.env` file in the root directory.

Example:

```env
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///passwords.db
FLASK_ENV=development
```

---

# 🐳 Docker Deployment

## Build Docker Image

```bash
docker build -t password-analyzer .
```

## Run Docker Container

```bash
docker run -p 8000:8000 password-analyzer
```

---

# 🌍 Production Deployment

Run the application using Gunicorn:

```bash
gunicorn -w 4 -b 0.0.0.0:8000 run:app
```

---

# 🧪 Testing & QA

## Run Automated Tests

```bash
pytest
```

## ✅ Testing Coverage

- Password validation testing
- API endpoint testing
- Security middleware testing
- Input sanitization testing
- Rate limiting verification
- Error handling validation

---

# 🎯 Learning Outcomes

This project helped strengthen my understanding of:

- 🔐 Password Security Mechanisms
- ⚡ Flask Backend Development
- 🌐 REST API Design
- 🛡️ Cybersecurity Best Practices
- 🗄️ Database Integration
- 🧪 Software Testing Workflows
- 🚀 Secure Production Deployment
- 🐳 Docker Containerization

---

# 🔮 Future Improvements

- 🐘 PostgreSQL Integration
- ⚡ Redis-Based Rate Limiting
- 🔑 JWT Authentication
- 📲 MFA / 2FA Support
- 🌍 Breached Password API Integration
- ☁️ Cloud Deployment Pipelines
- 📊 Admin Security Dashboard
- 🔔 Real-Time Threat Alerts

---

# 🤝 Contributing

Contributions are always welcome.

## 📌 Steps To Contribute

1️⃣ Fork the repository  
2️⃣ Create a feature branch  
3️⃣ Commit your changes  
4️⃣ Push your branch  
5️⃣ Open a Pull Request  

---

# 🌐 Connect With Me

<div align="center">

<a href="https://github.com/Mantechie">
<img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" />
</a>

<br><br>

<a href="https://www.linkedin.com/in/manan-sharma-24ab20229/">
<img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" />
</a>

</div>

---

# 👨‍💻 Author

<div align="center">

## Manan Sharma

🔐 Cybersecurity Enthusiast  
💻 Backend Developer  
⚡ Flask & API Developer  
🚀 Passionate About Secure Application Development

</div>

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

<div align="center">

## 🔐 Secure Code • Build Smart • Stay Protected

</div>

