

# 🏠 Home Energy Advisor

**Name:** GALGALO MOLU HALAKE
**Admission Number:** 669377
**Course:** APT3020B

---

## 📌 Project Overview

Home Energy Advisor is a web-based application designed to help users monitor and reduce their home energy consumption. The system provides Kenya-specific energy-saving recommendations, KSh-based billing estimates, and smart rule-based advice tailored to local energy usage patterns.

---

## 🛠️ Tech Stack

- **Backend:** Python (Flask)
- **Frontend:** HTML (Jinja2 Templates)
- **Database:** SQLite (`energy_advisor.db`)
- **Rule Engine:** Custom Python rule engine (`rule_engine.py`)

---

## 📁 Project Structure

```
home-energy-advisor/
│
├── templates/          # HTML templates
├── app.py              # Main Flask application
├── database.py         # Database setup and queries
├── energy_advisor.db   # SQLite database
├── rule_engine.py      # Energy rule logic
└── .gitignore
```

---

## ⚙️ How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/galgalo123/home-energy-advisor.git
   cd home-energy-advisor
   ```

2. **Install dependencies**
   ```bash
   pip install flask
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open in browser**
   ```
   http://127.0.0.1:5000
   ```

---

## 🌍 Features

- Kenya-specific energy saving rules
- KSh billing calculations
- Cooking and appliance usage recommendations
- SQLite-backed data persistence
- Simple and clean web interface

---