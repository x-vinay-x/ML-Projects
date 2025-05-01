# 🎯 Face Recognition-Based Attendance Monitoring System

![Face Recognition](https://img.shields.io/badge/Face%20Recognition-Active-blue)
![Firebase](https://img.shields.io/badge/Firebase-Integrated-orange)
![Python](https://img.shields.io/badge/Python-3.8+-yellow)
![OpenCV](https://img.shields.io/badge/OpenCV-Enabled-green)

## 🚀 Project Overview

This project is an **AI-powered Attendance Monitoring System** that uses **Face Recognition** to automate student or employee check-ins. Built using Python, OpenCV, and the `face_recognition` library, it leverages **Firebase** for real-time data storage and cloud integration.

### 🔍 Why This Project?
Manual attendance methods are time-consuming and prone to errors. Our system offers:
- Zero contact
- Instant recognition
- Realtime database sync
- Visual feedback using a dynamic GUI

---

## 🧠 Key Features

- ✅ Real-time face detection and recognition
- 📸 Automatic attendance logging
- 🔄 Firebase Realtime Database integration
- 🧑‍🎓 Student/employee image registration
- 📊 Stylish and interactive GUI (cvzone + OpenCV)
- ☁️ Cloud-based face data & attendance history

---

## 📁 Project Structure

```
facerecognition/
├── main.py                  # Entry point for live attendance
├── EncodeGenerator.py       # Converts face images into encodings
├── AddDataToDatabase.py     # Adds new user info to Firebase
├── EncodeFile.p             # Stored face encodings (pickle)
├── Images/                  # Folder of registered user photos
├── Resources/
│   ├── background.png       # Main GUI background
│   └── modes/               # Visual feedback modes
├── serviceAccountKey.json   # Firebase credentials
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/facerecognition-attendance.git
cd facerecognition-attendance
```

### 2. Install dependencies
Make sure you have Python 3.8+ installed.
```bash
pip install -r requirements.txt
```

### 3. Firebase Configuration
Replace `serviceAccountKey.json` with your own Firebase project's service key and update the database URL and bucket in `main.py`.

### 4. Run the system
```bash
python main.py
```

---

## 🖼️ Screenshots

| ![](https://github.com/x-vinay-x/ML-Projects/blob/main/Face%20Recognition-Based%20Attendance%20Monitoring%20System/Screenshot_1-5-2025_20454_.jpeg?raw=true) 
| ![](https://github.com/x-vinay-x/ML-Projects/blob/main/Face%20Recognition-Based%20Attendance%20Monitoring%20System/Screenshot_1-5-2025_20510_.jpeg?raw=true) 
| ![](Resources/sample_notfound.png) |

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

---

## 📬 Contact

Built with ❤️ by [VINAY N]

- GitHub: [x-vinay-x](https://github.com/yourusername)
- Email: vinevinayn@gmail.com

---

## 📜 License

This project is licensed under the MIT License.
