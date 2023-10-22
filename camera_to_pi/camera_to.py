import cv2
import socket
import pickle

def send_camera_feed():
    cap = cv2.VideoCapture(0)  # 0 for the built-in camera

    # Raspberry Pi's IP address and port
    rpi_ip = '100.64.118.231'
    rpi_port = 1234

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((rpi_ip, rpi_port))

        while True:
            ret, frame = cap.read()
            frame_serialized = pickle.dumps(frame)
            s.sendall(frame_serialized)

if __name__ == "__main__":
    send_camera_feed()
