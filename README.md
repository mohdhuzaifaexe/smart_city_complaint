# 🏙️ Smart City Complaint Management System

A web-based **Civic Complaint Management System** developed using **Python and Django**.

The system provides a digital platform where citizens can report civic problems such as street light issues, garbage, water supply problems, potholes, and other local issues. Citizens can track their complaints, while administrators can manage complaints and update their status.

---

## 📌 Project Overview

The **Smart City Complaint Management System** is designed to simplify the process of reporting and managing civic complaints.

Instead of handling complaints manually, the system provides an online platform where:

- Citizens can register and login
- Citizens can submit civic complaints
- Citizens can upload complaint images
- Citizens can track their complaints
- Citizens can view complete complaint details
- Administrators can manage complaints
- Administrators can update complaint status
- Administrators can monitor complaints through a dashboard
- Complaint statistics can be viewed using charts

---

## ✨ Features

### 👤 Citizen Features

- User Registration
- User Login and Logout
- Personal Dashboard
- Submit New Complaint
- Complaint Categories
- Location and Description
- Complaint Image Upload
- My Complaints
- Complaint Details
- Complaint Status Tracking
- Responsive Mobile Interface

### 👨‍💼 Admin Features

- Admin Authentication
- Admin Dashboard
- Total Complaint Statistics
- Pending Complaints
- In Progress Complaints
- Resolved Complaints
- Rejected Complaints
- Complaint Status Chart
- Complaints by Category Chart
- Manage Complaints
- Update Complaint Status
- Department Management
- Complaint Image Management

---

## 🔄 Complaint Workflow

```text
Citizen
   │
   ▼
Register / Login
   │
   ▼
Submit Complaint
   │
   ▼
Complaint Stored in Database
   │
   ▼
Admin Reviews Complaint
   │
   ▼
Pending
   │
   ▼
In Progress
   │
   ├───────────────┐
   ▼               ▼
Resolved        Rejected
   │               │
   └───────┬───────┘
           ▼
Citizen Tracks Updated Status
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend Programming |
| Django | Web Framework |
| SQLite | Database |
| HTML5 | Page Structure |
| CSS3 | Styling |
| Bootstrap 5 | Responsive UI |
| JavaScript | Client-side Functionality |
| Chart.js | Dashboard Charts |
| Pillow | Image Upload Handling |

---

## 📂 Project Structure

```text
smart_city_complaint/
│
├── complaints/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── my_complaints.html
│   ├── complaint_detail.html
│   └── admin_dashboard.html
│
├── static/
│   └── css/
│       └── style.css
│
├── media/
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the Project Directory

```bash
cd smart_city_complaint
```

### 3. Create Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

#### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply Database Migrations

```bash
python manage.py migrate
```

### 7. Create Admin Account

```bash
python manage.py createsuperuser
```

### 8. Start Development Server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

---

## 👨‍💼 Admin Access

After creating a superuser, open:

```text
http://127.0.0.1:8000/admin/
```

The administrator can:

- Manage users
- Manage complaints
- Manage categories
- Manage departments
- Update complaint status
- View uploaded complaint images

---

## 📊 Admin Dashboard

The Admin Dashboard provides an overview of complaint activity.

It displays:

- Total Complaints
- Pending Complaints
- In Progress Complaints
- Resolved Complaints
- Rejected Complaints
- Complaint Status Chart
- Complaints by Category Chart

---

## 🔐 Security & Access Control

The project uses **Django Authentication** for user management.

Different users have different access levels.

### Normal User

```text
Normal User
    │
    ├── Dashboard
    ├── Submit Complaint
    ├── My Complaints
    └── Complaint Details
```

### Admin / Staff

```text
Admin / Staff
    │
    ├── Admin Dashboard
    ├── Admin Panel
    └── Complaint Management
```

Normal users cannot access the Admin Dashboard without the required permissions.

---

## 📱 Responsive Design

The application uses **Bootstrap 5** and responsive CSS.

The interface is designed to work on:

- 💻 Desktop
- 💻 Laptop
- 📱 Mobile
- 📱 Tablet

The navigation menu also adapts to smaller screen sizes.

---

## 🖼️ Complaint Image Upload

Citizens can upload an image while submitting a complaint.

For example:

```text
Complaint
   │
   ├── Title
   ├── Category
   ├── Location
   ├── Description
   └── Image
```

Images are handled using the **Pillow** library and Django's media file system.

---

## 🔄 Complaint Status System

Each complaint can have different statuses:

| Status | Meaning |
|--------|---------|
| Pending | Complaint has been submitted and is waiting for processing |
| In Progress | Complaint is currently being processed |
| Resolved | Complaint has been successfully resolved |
| Rejected | Complaint has been rejected by the administrator |

---

## 🗄️ Database

The project currently uses **SQLite** as the database.

The database stores information such as:

- Users
- Complaints
- Categories
- Departments
- Complaint Status
- Complaint Images
- Complaint Dates

Django ORM is used to communicate with the database.

---

## 🎓 Academic Project

This project was developed as an academic **Python and Django project**.

The project demonstrates:

- Python Programming
- Django Framework
- Django ORM
- Database Management
- Authentication
- Authorization
- CRUD Operations
- Image/File Handling
- Role-Based Access Control
- Dashboard Development
- Data Visualization
- Responsive Web Design

---

## 🚀 Future Improvements

The system can be further improved by adding:

- 📧 Email Notifications
- 📱 SMS Notifications
- 📍 Google Maps Integration
- 📌 GPS-based Complaint Location
- 🔎 Advanced Search and Filtering
- ⚡ Complaint Priority System
- 🏢 Department-wise Dashboards
- ⭐ Citizen Feedback and Rating
- 🔌 REST API using Django REST Framework
- ☁️ Cloud Deployment
- 📊 Advanced Analytics

---

## 👨‍💻 Developer

**Mohd Huzaifa**

Diploma in Information Technology

---

## 📄 License

This project is developed for **educational and academic purposes**.