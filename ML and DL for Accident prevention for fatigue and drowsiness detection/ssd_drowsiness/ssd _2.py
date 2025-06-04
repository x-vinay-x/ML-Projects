import cv2
import numpy as np
import imutils
from imutils.video import VideoStream
from scipy.spatial import distance as dist
from imutils import face_utils
import dlib
import playsound
from threading import Thread
import time

from ssd_drowsiness.ssd_drowsiness import MOUTH_AR_CONSECUTIVE_FRAMES, audioalert, EYE_AR_THRESH, EYE_AR_CONSEC_FRAMES, \
    MOUTH_AR_THRESH, YELLOW_COLOR, eye_aspect_ratio, mouth_aspect_ratio, detect_and_predict_mask, getheadpose

# Load models
print("[INFO] loading face detector model...")
faceNet = cv2.dnn.readNet("deploy.prototxt", "face_detector.caffemodel")
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Grab facial landmark indices
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]
(mStart, mEnd) = face_utils.FACIAL_LANDMARKS_IDXS["mouth"]

# Function definitions omitted for brevity...

print("[INFO] starting video stream...")
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Use DirectShow backend
if not cap.isOpened():
    print("Error: Unable to access the camera")
    exit(1)

# Set desired resolution and frame rate
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 450)  # Reduced resolution
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 15)  # Reduced frame rate
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

time.sleep(2.0)  # Warm-up delay

while True:
    ret, frame = cap.read()
    if not ret or frame is None:
        print("Error: Unable to capture video from the camera.")
        break

    size = frame.shape
    frame = imutils.resize(frame, width=450)

    # Detect faces in the frame
    locs = detect_and_predict_mask(frame, faceNet)
    if len(locs) < 1:
        cv2.putText(frame, "Alert! No Driver", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    else:
        cv2.putText(frame, "", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # Loop over detected faces
    for box in locs:
        (x, y, w, h) = box
        rect = dlib.rectangle(int(x), int(y), int(w), int(h))
        shape = predictor(frame, rect)
        shape = face_utils.shape_to_np(shape)

        # Eye and mouth aspect ratio calculations
        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]
        mouth = shape[mStart:mEnd]
        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)
        mar = mouth_aspect_ratio(mouth)
        ear = (leftEAR + rightEAR) / 2.0

        # Visualize eyes and mouth
        mouthHull = cv2.convexHull(mouth)
        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)
        cv2.drawContours(frame, [mouthHull], -1, YELLOW_COLOR, 1)
        cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

        # Draw EAR and Yawn Count
        cv2.putText(frame, f"EAR: {ear:.2f}", (300, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        cv2.putText(frame, f"YAWN COUNT:{YAWN_COUNT}", (270, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        # Drowsiness detection logic
        if mar > MOUTH_AR_THRESH:
            MOUTH_COUNTER += 1
            if MOUTH_COUNTER >= MOUTH_AR_CONSECUTIVE_FRAMES:
                YAWN_COUNT += 1
                MOUTH_COUNTER = 0
                if YAWN_COUNT > 2:
                    cv2.imwrite("frame.jpg", frame)
                    audioalert()
                    YAWN_COUNT = 0
        else:
            MOUTH_COUNTER = 0

        if ear < EYE_AR_THRESH:
            COUNTER += 1
            if COUNTER >= EYE_AR_CONSEC_FRAMES:
                cv2.imwrite("frame.jpg", frame)
                audioalert()
        else:
            COUNTER = 0
            ALARM_ON = False

        # Head pose detection
        if get_pose:
            p1, p2 = getheadpose(frame, shape, size)
            pitch = p1[0]
            look = p2[1]
            if 150 < pitch < 200:
                cv2.putText(frame, "Looking Right", (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            elif 270 < pitch < 300:
                cv2.putText(frame, "Looking Left", (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            if 270 < look < 300:
                cv2.putText(frame, "Looking Down", (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            elif look < 100:
                cv2.putText(frame, "Looking Up", (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        cv2.putText(frame, "Face", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 255), 2)
        cv2.rectangle(frame, (x, y), (w, h), (0, 255, 0), 2)

    # Show the output frame
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    if key == ord("h"):
        get_pose = not get_pose

# Cleanup
cv2.destroyAllWindows()
cap.release()
print("[closed]")