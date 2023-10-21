import dlib
import cv2
import numpy as np

# Initialize the Dlib face detector
def biometrict():
    detector = dlib.get_frontal_face_detector()

    # Initialize the video capture
    cap = cv2.VideoCapture(0)  # You can specify a file path or device index (0 for the default camera)

    while True:
        # Read a frame from the video capture
        ret, frame = cap.read()

        # Convert the frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame using Dlib
        faces = detector(gray)

        # If a face is detected, quit the program
        if len(faces) == 1:
            face_rectangles = np.array([[rect.left(), rect.top(), rect.width(), rect.height()] for rect in faces])
            x, y, w, h = face_rectangles[0]
            detected_face = frame[y:y+h, x:x+w]
            print(detected_face)
            # print("Face detected. Quitting the program.")
            break

        # Display the frame with rectangles around detected faces
        for rect in faces:
            x, y, w, h = rect.left(), rect.top(), rect.width(), rect.height()
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the frame in a window
        cv2.imshow('Face Detection', frame)

        # Break the loop if the user presses the 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()




