# import cv2
# import mediapipe as mp

# def main():
#     # Initialize MediaPipe Hand module
#     mp_hands = mp.solutions.hands
#     hands = mp_hands.Hands()

#     # Initialize MediaPipe Drawing module for visualizing landmarks
#     mp_drawing = mp.solutions.drawing_utils

#     # Initialize webcam capture
#     cap = cv2.VideoCapture(0)

#     if not cap.isOpened():
#         print("Error: Could not open the camera.")
#         return

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break

#         # Flip the frame horizontally for a later selfie-view display
#         frame = cv2.flip(frame, 1)

#         # Convert the BGR image to RGB
#         frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#         # Process the frame with MediaPipe Hands
#         results = hands.process(frame_rgb)

#         if results.multi_hand_landmarks:
#             for hand_landmarks in results.multi_hand_landmarks:
#                 # Draw hand landmarks and connections on the frame
#                 mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                

#         # Display the video feed with hand landmarks
#         cv2.imshow("Hand Gestures", frame)

#         # Press 'Esc' to exit the program
#         if cv2.waitKey(1) & 0xFF == 27:
#             break

#     cap.release()
#     cv2.destroyAllWindows()

# if __name__ == "__main__":
#     main()

# import cv2
# import mediapipe as mp
# import numpy as np

# def main():
#     mp_hands = mp.solutions.hands
#     hands = mp_hands.Hands()

#     mp_drawing = mp.solutions.drawing_utils

#     cap = cv2.VideoCapture(0)

#     if not cap.isOpened():
#         print("Error: Could not open the camera.")
#         return

#     # Load and preprocess your gesture images
#     # Load and preprocess your gesture images
#     gesture_images = cv2.convertScaleAbs(cv2.imread('/Users/soldire/Documents/HackTX2023/thumbs_down.jpg', cv2.IMREAD_GRAYSCALE))

# # Load and preprocess your gesture images

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break

#         frame = cv2.flip(frame, 1)
#         frame_rgb = frame

#         results = hands.process(frame_rgb)

#         if results.multi_hand_landmarks:
#             for hand_landmarks in results.multi_hand_landmarks:
#                 mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

#         # Iterate through your gesture images and perform template matching
#         for gesture_img in gesture_images:
#             result = cv2.matchTemplate(frame, gesture_img, cv2.TM_CCOEFF_NORMED)
#             min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

#             # You can set a threshold to consider a match
#             threshold = 0.7  # Adjust as needed
#             if max_val > threshold:
#                 # Match found, you can take action here
#                 print("Gesture detected!")

#         cv2.imshow("Hand Gestures", frame)

#         if cv2.waitKey(1) & 0xFF == 27:
#             break


# if __name__ == "__main__":
#     main()

# import cv2
# import mediapipe as mp

# # Initialize MediaPipe Hands
# mp_hands = mp.solutions.hands
# hands = mp_hands.Hands()

# # Initialize MediaPipe Drawing
# mp_drawing = mp.solutions.drawing_utils

# # Define colors
# GREEN = (0, 255, 0)
# RED = (0, 0, 255)

# # Open the webcam
# cap = cv2.VideoCapture(0)

# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         continue

#     # Convert the BGR image to RGB
#     frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#     # Process the frame to detect hands
#     results = hands.process(frame_rgb)

#     if results.multi_hand_landmarks:
#         for landmarks in results.multi_hand_landmarks:
#             # Extract landmarks for thumb and other fingers
#             thumb_tip = landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
#             index_finger_tip = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

#             # Calculate the distance between thumb tip and index finger tip
#             distance = cv2.norm((int(thumb_tip.x * frame.shape[1]), int(thumb_tip.y * frame.shape[0])),
#                                 (int(index_finger_tip.x * frame.shape[1]), int(index_finger_tip.y * frame.shape[0])))

#             # Detect thumbs-up gesture
#             if distance > 350:
#                 cv2.putText(frame, "Thumbs Up", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, GREEN, 2)
#                 cv2.line(frame, (20, 60), (frame.shape[1] - 20, 60), GREEN, 5)
#             else:
#                 cv2.putText(frame, "Not Thumbs Up", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, RED, 2)
#                 cv2.line(frame, (20, 60), (frame.shape[1] - 20, 60), RED, 5)

#     # Display the frame with annotations
#     cv2.imshow('Thumbs Up Detection', frame)

#     if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
#         break

# cap.release()
# cv2.destroyAllWindows()

import cv2
import mediapipe as mp

def main():
    # Initialize MediaPipe Hand module
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()

    # Initialize MediaPipe Drawing module for visualizing landmarks
    mp_drawing = mp.solutions.drawing_utils

    # Define colors
    GREEN = (0, 255, 0)
    RED = (0, 0, 255)

    # Initialize webcam capture
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open the camera.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Flip the frame horizontally for a later selfie-view display
        frame = cv2.flip(frame, 1)

        # Convert the BGR image to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame with MediaPipe Hands
        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw hand landmarks and connections on the frame
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Extract landmarks for thumb and index finger
                thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

                # Calculate the distance between thumb tip and index finger tip
                distance = ((thumb_tip.x - index_finger_tip.x) ** 2 + (thumb_tip.y - index_finger_tip.y) ** 2) ** 0.5

                # Check if the distance is below a threshold (closed fist)
                threshold = 0.05  # Adjust this threshold as needed
                if distance < threshold:
                    cv2.putText(frame, "Closed Fist", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, GREEN, 2)
                    cv2.line(frame, (20, 60), (frame.shape[1] - 20, 60), GREEN, 5)
                else:
                    cv2.putText(frame, "Open Palm", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, RED, 2)
                    cv2.line(frame, (20, 60), (frame.shape[1] - 20, 60), RED, 5)

        # Display the video feed with hand landmarks
        cv2.imshow("Hand Gestures", frame)

        # Press 'Esc' to exit the program
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
