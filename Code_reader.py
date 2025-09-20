from time import sleep
import cv2 # read image/camera/video input
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
cap.set(3, 640)   # 3 - Width
cap.set(4, 480)   # 4 - Height
used_codes = []

camera = True
while camera == True:
    succes, frame = cap.read()

    for code in decode(frame):
        content = code.data.decode('utf8')
        if content not in used_codes:
            print('Approuved. You can enter !')
            print(content)
            used_codes.append(content)
            sleep(5)
        elif content is used_codes:
            print('Sorry, this code has been already used !')
            sleep(5)
        else:
            pass


    cv2.imshow('Testing-code-scan', frame)
    cv2.waitKey(1)

