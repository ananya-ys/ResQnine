# SheShield AI

Voice Activated Emergency Safety System

## Setup

1. Clone the repository

2. Create virtual environment

python -m venv venv

3. Activate environment

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

4. Install dependencies

pip install -r requirements.txt

5. Create environment file

Copy `.env.example` → `.env`

6. Verify setup

python verify_setup.py

7. Run server

uvicorn app.main:app --reload