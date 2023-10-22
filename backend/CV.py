import cv2
import mediapipe as mp
import screen_brightness_control as sbc

def main():
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()
    mp_drawing = mp.solutions.drawing_utils
    GREEN = (0, 255, 0)
    RED = (0, 0, 255)

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open the camera.")
        return

    brightness_increase = 1

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Flip the frame horizontally for a later selfie-view display
        frame = cv2.flip(frame, 1)

        # Convert the BGR image to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

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
                
                if(distance < 0.085):
                    brightness_increase = 1
                elif(distance < 0.16 and distance >= 0.085):
                    brightness_increase = 2
                elif(distance < 0.25 and distance >= 0.16):
                    brightness_increase = 3
                elif(distance < 0.35 and distance >= 0.25):
                    brightness_increase = 4

                # Check if the distance is below a threshold (closed fist)
                threshold = 0.05
                if distance < threshold:
                    cv2.putText(frame, "Decrease Light", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, GREEN, 2)
                    cv2.line(frame, (20, 60), (frame.shape[1] - 20, 60), GREEN, 5)
                    brightness_levels = sbc.get_brightness()
                    # Decrease screen brightness
                    if brightness_levels:
                        current_brightness = brightness_levels[0]
                    if current_brightness <= 100 and current_brightness > 0:
                        sbc.set_brightness(current_brightness - brightness_increase)
                    if current_brightness > 100 or current_brightness <= 0:
                        sbc.set_brightness(current_brightness)
                else:
                    if(distance < 0.085):
                        brightness_increase = 1
                    elif(distance < 0.16 and distance >= 0.085):
                        brightness_increase = 2
                    elif(distance < 0.25 and distance >= 0.16):
                        brightness_increase = 3
                    elif(distance < 0.35 and distance >= 0.25):
                        brightness_increase = 4
                    cv2.putText(frame, "Increase Light", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, RED, 2)
                    cv2.line(frame, (20, 60), (frame.shape[1] - 20, 60), RED, 5)
                    # Restore original screen brightness
                    brightness_levels = sbc.get_brightness()
                    # Increase screen brightness
                    if brightness_levels:
                        current_brightness = brightness_levels[0]
                    if current_brightness < 100 and current_brightness >= 0:
                        sbc.set_brightness(current_brightness + brightness_increase)
                    if current_brightness >= 100 or current_brightness < 0:
                        sbc.set_brightness(current_brightness)

        # Display the video feed with hand landmarks
        cv2.imshow("Hand Gestures", frame)

        # Press 'Esc' to exit the program
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
