#  🛡️ Driver Drowsiness Detection System

<p align="center">
  <img src="https://img.shields.io/badge/python-3.6+-blue.svg">
  <img src="https://img.shields.io/badge/OpenCV-Real--Time-green">
  <img src="https://img.shields.io/badge/Dlib-FacialLandmarks-yellow">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen">
</p>

> 🚗💤 An intelligent system to detect drowsiness and alert drivers in real time using computer vision and deep learning!

---

## 🧠 What is this?

This project is a **real-time drowsiness detection system** that monitors a driver's face through a webcam to detect signs of fatigue like prolonged eye closure and yawning. Once drowsiness is detected, a voice alert is triggered to warn the driver — potentially preventing road accidents caused by sleepiness behind the wheel.

---

## 🌟 Features

✅ Real-time face detection using a pre-trained SSD (Single Shot Detector)  
✅ 68-point facial landmark recognition using Dlib  
✅ Eye Aspect Ratio (EAR) and Mouth Aspect Ratio (MAR) calculations  
✅ Voice alert (`voice.mp3`) when drowsiness is detected  
✅ Easy to run and lightweight for embedded systems or laptops

---

## 📂 Project Structure

```
📁 driver_drowsiness_detection/
├── ssd_drowsiness.py                  # 🎯 Main script for detection
├── ssd _2.py                          # 🧪 Alternate/experimental version
├── sample_code.txt                    # 🧾 Miscellaneous code snippets
├── voice.mp3                          # 🔊 Audio alert on fatigue detection
│
├── deploy.prototxt                    # 📄 SSD model config
├── face_detector.caffemodel           # 🧠 Pre-trained face detector
├── shape_predictor_68_face_landmarks.dat  # 📌 Facial landmark model (Dlib)
└── ssd_drowsiness.cpython-38.pyc      # ⚙️ Compiled Python file (optional)
```

---

## ⚙️ Installation

1. Clone this repository:
```bash
git clone https://github.com/your-username/driver-drowsiness-detection.git
cd driver-drowsiness-detection
```

2. Install dependencies:
```bash
pip install opencv-python dlib numpy imutils playsound
```

> ⚠️ Make sure Dlib and CMake are properly configured on your machine.

---

## 🚀 How to Run

Make sure your webcam is connected and run the main script:

```bash
python ssd_drowsiness.py
```

The script will:
- Detect your face
- Analyze facial landmarks
- Monitor eye and mouth movements
- Play `voice.mp3` if drowsiness is detected

---

## 🧪 How It Works

| Module | Function |
|--------|----------|
| 🔍 **Face Detection** | SSD Caffe model locates the face in real-time |
| 📌 **Facial Landmark Detection** | Dlib detects key points (eyes, nose, mouth, etc.) |
| 👁️ **EAR (Eye Aspect Ratio)** | Measures eye openness; detects closed eyes |
| 👄 **MAR (Mouth Aspect Ratio)** | Detects yawning via lip distance |
| 🚨 **Alert System** | Plays an audio alert if drowsiness is sustained |

> 🧬 If the EAR drops below a certain threshold or MAR increases beyond normal yawning range for several frames, the system triggers an alarm.

---

## 🔊 Voice Alert

A customizable `voice.mp3` is played through the speaker to alert the driver. You can change this file to any `.mp3` format voice message of your choice.

---

## 💡 Applications

- Advanced Driver Assistance Systems (ADAS)
- Long-haul trucking safety
- Automotive R&D
- Academic projects and CV workshops

---

## 🙏 Credits

- 💻 [OpenCV](https://opencv.org/)
- 🧠 [Dlib](http://dlib.net/)
- 📦 Pre-trained models from the OpenCV model zoo and Dlib

---

## 📜 License

This project is licensed under the **MIT License** - you're free to use, modify, and distribute it.

---

⭐️ Star this repo if you find it helpful!  
Made with ❤️ by [VINAY N]
