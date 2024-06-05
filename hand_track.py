import cv2
from cvzone.HandTrackingModule import HandDetector

frame = cv2.VideoCapture(0)
frame.set(3, 1280)
frame.set(4, 720)

handDetector = HandDetector(detectionCon=0.8)

while True:

    res, img = frame.read()

    hands = handDetector.findHands(img)

    cv2.imshow("Virtual Zoom Gesture", img)
    cv2.waitKey(1)

