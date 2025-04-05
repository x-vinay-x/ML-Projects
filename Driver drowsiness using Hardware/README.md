# 🛡️ Driver Drowsiness Detection System (AI + Arduino + GSM)

<p align="center">
  <img src="https://img.shields.io/badge/python-3.8+-blue.svg">
  <img src="https://img.shields.io/badge/OpenCV-Real--Time-green">
  <img src="https://img.shields.io/badge/Dlib-FacialLandmarks-yellow">
  <img src="https://img.shields.io/badge/GSM-SIMA7670C-blueviolet">
  <img src="https://img.shields.io/badge/Status-Prototype-brightgreen">
</p>

> 🚗💤 An AI-powered system that detects driver drowsiness in real time and triggers **GSM alerts**, buzzer alarms, and visual indicators using Arduino!

---

## 🧠 What is this?

This project is a **real-time driver drowsiness detection system** using computer vision and hardware integration via Arduino. It monitors a driver's face using a webcam and AI to detect sleepiness. When drowsiness is detected, it sends a signal to an Arduino, which activates a **buzzer, LED, and sends an SMS alert via a GSM module** (SIMA7670C or similar).

---

## 🌟 Features

✅ Real-time facial landmark detection using Dlib  
✅ Eye Aspect Ratio (EAR) for detecting closed eyes  
✅ GSM-based SMS alert to emergency contacts  
✅ Serial communication from Python to Arduino  
✅ Buzzer and LED for immediate hardware alerts  
✅ Compact and deployable on embedded systems  

---

## 📂 Project Structure

```
📁 drowsiness-detection/
├── sample.py                             # 🧠 Python script (AI + Serial Comm)
├── sketch_01.ino                         # 🔌 Arduino code (GSM + buzzer + LED)
├── shape_predictor_68_face_landmarks.dat # 📌 Dlib landmark model
├── haarcascade_frontalface_default.xml  # 👤 Haar cascade face detector
```

---

## ⚙️ Installation

1. Clone this repo:
```bash
git clone https://github.com/your-username/drowsiness-detection-arduino-gsm.git
cd drowsiness-detection-arduino-gsm
```

2. Install Python dependencies:
```bash
pip install opencv-python dlib imutils numpy scipy pyserial
```

---

## 🚀 How to Run

### 1. Upload Arduino Code

- Open `sketch_01.ino` in the Arduino IDE
- Connect your **Arduino + GSM module (e.g. SIMA7670C)** + buzzer + LED
- Upload the code

> 🔧 Don't forget to insert a valid SIM card into your GSM module

### 2. Run the Python script

```bash
python sample.py
```

> ✅ Make sure the serial port in `sample.py` matches your Arduino’s port (e.g., COM6 or /dev/ttyUSB0)

---

## 🧪 How It Works

| Component | Function |
|----------:|----------|
| 🎥 Webcam | Captures live video of the driver |
| 👁️ Dlib | Detects eye landmarks to compute EAR |
| ⚠️ EAR | Low EAR for a few seconds means sleepiness |
| 🧠 Python | Sends 'a' (drowsy) or 'b' (awake) to Arduino |
| 🔔 Arduino | Activates buzzer, LED, and GSM SMS alerts |

---

## 📲 GSM SMS Alert

When drowsiness is detected:

- Arduino receives `'a'` over serial
- Buzzer and LED turn ON
- **An SMS is sent** to your configured mobile number using the GSM module:
  ```
  "Alert: Drowsiness detected! Please check on the driver."
  ```

To customize the phone number or message:
```cpp
// In sketch_01.ino
mySerial.println("AT+CMGS=\"+911234567890\"\r");  // Replace with your number
```

---

## 📸 Visual Output

The Python GUI will show:
- 😴 "SLEEPING !!!" in red  
- 😐 "Drowsy !" in red  
- 😀 "Active :)" in green  

---

## 💡 Applications

- Automotive driver assistance systems (ADAS)  
- Fleet safety and monitoring  
- Public transport and logistics safety  
- Sleep detection in industrial environments  

---

## 🙏 Credits

- [OpenCV](https://opencv.org/)  
- [Dlib](http://dlib.net/)  
- [Arduino](https://www.arduino.cc/)  
- EAR method inspired by Soukupová & Čech, CVWW 2016  
- GSM based on SIM800 AT commands  

---

## 📜 License

MIT License. Free to use, modify, and distribute.

---

⭐️ Star this repo if you like it!  
Made with ❤️ by [VINAY N]
