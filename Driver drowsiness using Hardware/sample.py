import cv2
import numpy as np
from scipy.spatial import distance as dist
from imutils import face_utils
import dlib
import serial
import time

# Initialize serial connection
try:
    s = serial.Serial('COM6', 115200, timeout=1)  # Match baud rate with Arduino
except serial.SerialException as e:
    print(f"Error opening serial port: {e}")
    exit(1)

# Start the video capture
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)  # Use DirectShow backend
if not cap.isOpened():
    print("Error: Unable to access the camera")
    s.close()
    exit(1)

# Set desired resolution and frame rate
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 450)  # Reduced resolution
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 15)  # Reduced frame rate
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

# Load face detector and landmark predictor
hog_face_detector = dlib.get_frontal_face_detector()
try:
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
except Exception as e:
    print(f"Error loading shape predictor: {e}")
    cap.release()
    s.close()
    exit(1)

# Grab the indexes of the facial landmarks for the left and right eye
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

# Status tracking variables
sleep, drowsy, active = 0, 0, 0
status, prev_status = "", None
color = (0, 0, 0)

# Thresholds for faster reaction
EYE_AR_THRESH = 0.25
EYE_AR_CONSEC_FRAMES = 20  # Reduced threshold for faster detection
ACTIVE_THRESHOLD = 3


def compute(ptA, ptB):
    """Compute Euclidean distance between two points."""
    return np.linalg.norm(ptA - ptB)


def blinked(a, b, c, d, e, f):
    """Determine blink state based on eye landmarks."""
    up = compute(b, d) + compute(c, e)
    down = compute(a, f)
    ratio = up / (2.0 * down)

    # Return blink state: 0 = closed, 1 = drowsy, 2 = open
    return 2 if ratio > 0.25 else 1 if ratio > 0.21 else 0


def send_serial_command(command):
    """Send data to Arduino only if status changes."""
    global prev_status
    if command != prev_status:
        try:
            s.write(command.encode())
            prev_status = command
            print(f"Sent command: {command}")  # Debugging: Print sent command
        except serial.SerialException as e:
            print(f"Serial communication error: {e}")


try:
    # Discard initial frames to clear buffer
    for _ in range(5):
        ret, _ = cap.read()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to capture video")
            break

        # Preprocess the frame
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)  # Reduce noise
        gray = cv2.equalizeHist(gray)  # Enhance contrast

        faces = hog_face_detector(gray)

        for face in faces:
            landmarks = predictor(gray, face)
            landmarks = face_utils.shape_to_np(landmarks)

            # Detect left and right eye blinks
            left_blink = blinked(
                landmarks[36], landmarks[37], landmarks[38],
                landmarks[41], landmarks[40], landmarks[39]
            )
            right_blink = blinked(
                landmarks[42], landmarks[43], landmarks[44],
                landmarks[47], landmarks[46], landmarks[45]
            )

            # Update counters based on blink state
            if left_blink == 0 or right_blink == 0:  # Eyes closed
                sleep += 1
                drowsy = 0
                active = 0
                if sleep > EYE_AR_CONSEC_FRAMES:
                    send_serial_command('a')
                    status, color = "SLEEPING !!!", (0, 0, 255)
            elif left_blink == 1 or right_blink == 1:  # Drowsy
                sleep = 0
                active = 0
                drowsy += 1
                if drowsy > EYE_AR_CONSEC_FRAMES:
                    send_serial_command('a')
                    status, color = "Drowsy !", (0, 0, 255)
            else:  # Eyes fully open
                sleep = 0
                drowsy = 0
                active += 1
                if active > ACTIVE_THRESHOLD:
                    send_serial_command('b')
                    status, color = "Active :)", (0, 255, 0)

            # Display status on the frame
            cv2.putText(frame, status, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)

        # Show the frame
        cv2.imshow("Frame", frame)

        # Exit on ESC key press
        if cv2.waitKey(1) & 0xFF == 27:
            break

finally:
    # Release resources
    cap.release()
    cv2.destroyAllWindows()
    s.close()