import cv2 # read image/camera/video input
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
cap.set(3, 640)   # 3 - Width
cap.set(4, 480)   # 4 - Height
camera = True
while camera == True:
    succes, frame = cap.read()

    for code in decode(frame):
        print(code.type)
        print(code.data.decode('utf8'))

    cv2.imshow('Testing-code-scan', frame)
    cv2.waitKey(1)

