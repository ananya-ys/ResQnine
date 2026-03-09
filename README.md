# SheShield AI 🚨

### Voice-Activated Emergency Safety System

SheShield AI is an emergency safety platform designed to help users quickly alert trusted guardians during dangerous situations. The system can trigger emergency alerts, share the user’s location, and notify guardians instantly through automated alert services.

This project was developed as part of a hackathon to demonstrate how technology can improve personal safety and rapid emergency response.

---

# 🚀 Features

* 🎤 **Voice-Activated Emergency Trigger**
  Users can activate emergency mode through a voice command.

* 🚨 **Panic Mode Activation**
  Instantly triggers emergency alerts.

* 📍 **Location Sharing**
  Captures the user's location and sends it to guardians.

* 📩 **Guardian Alert System**
  Sends alerts through backend alert services.

* ⚡ **FastAPI Backend**
  Lightweight and high-performance backend built with FastAPI.

* 🌐 **Web Dashboard**
  Simple interface for interacting with the system.

---

# 🏗 Tech Stack

**Backend**

* Python
* FastAPI

**Frontend**

* HTML
* CSS
* JavaScript

**Tools**

* Git
* GitHub
* VS Code

**Optional Integrations**

* SMS APIs (Twilio or similar)
* Email notification services

---

# 📂 Project Structure

```
SheShield-AI
│
├── backend
│   ├── app
│   │   ├── api
│   │   ├── core
│   │   ├── exceptions
│   │   ├── schemas
│   │   └── services
│   │       └── alert_service.py
│   │
│   ├── main.py
│   └── requirements.txt
│
├── frontend
│   ├── css
│   ├── dashboard.html
│   ├── guardian.html
│   └── index.html
│
├── .env.example
├── verify_setup.py
└── README.md
```

---

# ⚙️ Setup

## 1. Clone the repository

```
git clone https://github.com/ananya-ys/SheShield-AI.git
cd SheShield-AI
```

---

## 2. Create virtual environment

```
python -m venv venv
```

---

## 3. Activate environment

Windows

```
venv\Scripts\activate
```

Mac / Linux

```
source venv/bin/activate
```

---

## 4. Install dependencies

```
pip install -r requirements.txt
```

---

## 5. Create environment file

Copy the example environment configuration:

```
.env.example → .env
```

Then update the variables inside `.env` with your local configuration.

---

## 6. Verify setup

Run the setup verification script:

```
python verify_setup.py
```

This checks if the environment and dependencies are configured correctly.

---

## 7. Run the server

Start the backend server using:

```
uvicorn app.main:app --reload
```

The API will run at:

```
http://127.0.0.1:8000
```

API documentation will be available at:

```
http://127.0.0.1:8000/docs
```

---

# 📢 Example Emergency Alert

```
🚨 EMERGENCY ALERT

User may be in danger.

Location:
MG Road, Bangalore

Coordinates:
12.9716, 77.5946

Open in Maps:
https://maps.google.com/?q=12.9716,77.5946
```

---

# 👩‍💻 My Contribution

* Implemented backend architecture using **FastAPI**
* Developed the **alert service logic**
* Designed the **project structure and backend workflow**
* Integrated **frontend with backend APIs**

---

# 🔮 Future Improvements

* Real-time location tracking
* Mobile app integration
* AI-based threat detection
* Direct emergency service integration
* Voice recognition improvements

---

# ⚠️ Disclaimer

This project was developed as part of a hackathon to demonstrate the concept of an AI-powered emergency safety system. It is intended for educational and demonstration purposes.
