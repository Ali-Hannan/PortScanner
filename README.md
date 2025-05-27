# 🔍 Port Scanner Web App

A modern full-stack port scanner built using **React.js** (frontend) and **Flask (Python)** (backend). This application allows users to input a hostname and a list of ports, then scans them in real-time to display whether each port is open or closed—enhanced with icons, tooltips, fun facts, and animated results.

---

## 🚀 Features

- 🔄 Real-time port scanning using Python's `socket` module
- 🎯 RESTful API with Flask
- ⚡ React.js frontend with fetch integration
- 🖌️ Responsive, modern UI styled with custom CSS
- 🔐 Visual indicators: 🔓 for open, 🔒 for closed ports
- 💬 Hover tooltips for extra context
- 🌀 Loading spinner during scans
- 📱 Mobile-friendly layout

---

## 🧠 Tech Stack

| Layer      | Tech       |
|------------|------------|
| Frontend   | React.js (Vite) |
| Backend    | Flask (Python) |
| Styling    | Custom CSS |
| Communication | REST API + Fetch |
| Extras     | Flask-CORS, Socket module, Postman (for testing)

---

## 🛠️ How It Works

1. User inputs a hostname (e.g. `scanme.nmap.org`) and comma-separated ports (e.g. `21, 22, 80`).
2. Frontend sends a POST request to the Flask backend.
3. Flask scans the ports using Python's socket module.
4. Backend responds with scan results (status, service, and fun facts).
5. Frontend displays results with icons and animations.

---

## 📷 Screenshots

![image](https://github.com/user-attachments/assets/01f6f323-3712-4c49-884b-06ebb959c58d)


![image](https://github.com/user-attachments/assets/7459f757-55d7-4d70-8cfe-d0cfe0e3122f)



---


📝 Future Improvements

    🌍 Deploy frontend (Netlify/Vercel) and backend (Render/Railway)

    📊 Scan history logging

    🧑‍💻 Authentication for premium scanning

    ☁️ Save or download results



## 📦 Getting Started

### 🖥 Backend Setup (Flask) and Frontend Step (React)

```bash
cd backend
pip install flask flask-cors
python api.py
```

### 🌐 Frontend Setup (React)

```bash
cd frontend
npm install
npm run dev
```

### 🧪 Example Input

```bash
{
  "host": "scanme.nmap.org",
  "ports": [21, 22, 80]
}
```

### 👨‍💻 Author

Hannan Ali
💼 Full Stack Developer

🔗 https://www.linkedin.com/in/alihannan/

📧 hannan@cyranixtech.com
