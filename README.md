# GreenGuard AI — Malicious Website Detection System

## Fix for requirements.txt error
Make sure you are inside the folder containing `manage.py` and `requirements.txt`.

## Windows PowerShell
```powershell
cd "C:\xampp\htdocs\Malicious_Website_Detection_AI_Green"
python -m venv venv
.\venv\Scripts\python.exe -m pip install -r requirements.txt
.\venv\Scripts\python.exe train_model.py
.\venv\Scripts\python.exe manage.py migrate
.\venv\Scripts\python.exe manage.py createsuperuser
.\venv\Scripts\python.exe manage.py runserver
```

Open https://malicious-website-detection-ai-green.onrender.com

## Features
- URL-only malicious website detection
- Random Forest ML model
- Login/register
- Prediction history
- Dashboard with animated Chart.js chart
- Green security-themed responsive UI
- CSS animations and hover effects
- Django admin

The training dataset is synthetic/demo data for academic presentation. Replace it with a properly licensed real dataset for research evaluation. The system analyzes URL strings/features and does not automatically visit unknown websites.
