# Secure File Vault

A web-based secure file storage system developed using Flask and SQLite.

This project demonstrates core Information System Security concepts including:

- User Authentication
- Password Hashing
- File Encryption
- Secure Storage
- Session Management
- Access Control

---

# Project Overview

Secure File Vault allows users to create accounts, upload files securely, and retrieve them later.

Uploaded files are encrypted before being stored on disk to reduce exposure in case of unauthorized access.

The system was developed as an Information System Security course project.

---

# Features

## Authentication
- User Registration
- User Login
- Session Handling
- Password Hashing using bcrypt
- Duplicate Username Prevention

## File Security
- File Upload
- Automatic Encryption
- Secure Storage
- File Download and Decryption

## System Security
- Database Constraints
- Access Restriction
- Error Handling

---

# Technologies Used

| Component | Technology |
|----------|-----------|
| Backend | Flask |
| Database | SQLite |
| ORM | SQLAlchemy |
| Password Security | Flask-Bcrypt |
| Encryption | Cryptography (Fernet AES) |
| Frontend | HTML + CSS |

---

# System Architecture

```plaintext
User
 ↓
Login/Register
 ↓
Authentication
 ↓
Secure Dashboard
 ↓
Upload File
 ↓
Encryption
 ↓
Encrypted Storage
 ↓
Download
 ↓
Decryption
```

---

# Folder Structure

```plaintext
secure-file-vault/

│
├── app.py
├── encryption.py
├── requirements.txt
├── vault.db
│
├── uploads/
│
├── static/
│   └── style.css
│
└── templates/
    ├── login.html
    ├── register.html
    └── dashboard.html
```

---

# Installation

## Clone Project

```bash
git clone <repository-url>
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run

```bash
python app.py
```

Open:

```plaintext
http://127.0.0.1:5000
```

---

# Usage

## Register
Create an account.

## Login
Authenticate with username and password.

## Upload
Choose a file to upload.

The system encrypts the file before saving.

## Download
Retrieve and decrypt files.

---

# Database Design

## User Table

| Field | Type |
|------|------|
| id | Integer |
| username | String |
| password | String |

## File Table

| Field | Type |
|------|------|
| id | Integer |
| filename | String |
| owner | String |

---

# Security Mechanisms

## Password Protection
Passwords are stored using bcrypt hashing.

## File Encryption
Files are encrypted using Fernet symmetric encryption.

## Authentication
Only authenticated users can access the vault.

## Access Control
Each user only sees their uploaded files.

---

# Threats Addressed

- Unauthorized file access
- Plaintext storage
- Password theft
- Duplicate account abuse

---

# Future Improvements

- Multi-Factor Authentication (MFA)
- File Sharing
- Admin Dashboard
- Audit Logs
- Cloud Deployment
- File Expiration
- Malware Scanning

---

# Limitations

- Local deployment only
- Single encryption key
- No password recovery

---

# Conclusion

Secure File Vault demonstrates how common information system security techniques can be applied in a practical web application.

The project integrates authentication, encryption, and secure storage principles into a functional file management system.