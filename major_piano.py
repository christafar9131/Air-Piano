import cv2
import mediapipe as mp
# import numpy as np
import pygame

# Initialize MediaPipe Hands module
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Define piano keys (C4 to B4)
keys = ["C", "D", "E", "F", "G", "A", "B"]
key_width, key_height = 90, 200
  # Path to sound files

# Function to draw the virtual piano
def draw_piano(img):
    for i, key in enumerate(keys):
        x = i * key_width + 50
        cv2.rectangle(img, (x, 300), (x + key_width, 500),-1)
        cv2.rectangle(img, (x, 300), (x + key_width, 500), (0, 0, 0), 2)
        cv2.putText(img, key, (x + 30, 480), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Function to detect key press
def detect_key_press(x, y):
    if 300 < y < 500:  # Only detect presses in the piano area
        for i, key in enumerate(keys):
            x1, x2 = i * key_width + 50, (i + 1) * key_width + 50
            if x1 < x < x2:
                return key
    return None

# Function to play piano sounds
def play_sound(note):
    pygame.mixer.init()
    pygame.mixer.music.load(f"sounds/{note}.wav")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        if pygame.mixer.music.play():
            continue  # Keep script running until sound finishes
        else:
            break

# Start video capture
cap = cv2.VideoCapture(0)

# Hand detection
with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Flip and convert frame
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process hand tracking
        results = hands.process(rgb_frame)

        # Draw piano on screen
        draw_piano(frame)

        # Detect fingertip (Index Finger - Landmark 8)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                index_finger_tip = hand_landmarks.landmark[8]
                h, w, _ = frame.shape
                x, y = int(index_finger_tip.x * w), int(index_finger_tip.y * h)

                # Draw fingertip position
                cv2.circle(frame, (x, y), 10, (0, 255, 0), -1)

                # Detect key press
                key = detect_key_press(x, y)
                if key:
                    play_sound(key)
                    cv2.putText(frame, f"Playing: {key}", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Display the frame
        cv2.imshow("Virtual Piano", frame)

        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release resources
cap.release()
cv2.destroyAllWindows()