import cv2
import mediapipe as mp
import numpy as np

# Load the "thumbs-up" image you want to detect
thumbs_up_image = cv2.imread('open_palm.jpg')

# Function to check if a frame contains the "thumbs-up" gesture
def is_thumbs_up(frame):
    # Initialize MediaPipe Hand module
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()

    # Convert the BGR image to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe Hands
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

            # Check if the thumb tip is above the index finger tip (thumbs-up gesture)
            if thumb_tip.y < index_finger_tip.y:
                return True

    return False

# Initialize webcam capture
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open the camera.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally for a later selfie-view display
    frame = cv2.flip(frame, 1)

    # Check if the frame contains the "thumbs-up" gesture
    if is_thumbs_up(frame):
        cv2.putText(frame, "Thumbs Up", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    else:
        cv2.putText(frame, "Not Thumbs Up", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Display the video feed
    cv2.imshow("Hand Gestures", frame)

    # Press 'Esc' to exit the program
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
