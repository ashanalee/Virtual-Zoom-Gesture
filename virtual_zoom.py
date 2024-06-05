import cv2
from cvzone.HandTrackingModule import HandDetector

frame = cv2.VideoCapture(0)
frame.set(3, 1280)
frame.set(4, 720)

handDetector = HandDetector(detectionCon=0.8)
distStart = None
zoom_range = 0
cx, cy = 500, 500

while True:
    res, img = frame.read()

    hands, img = handDetector.findHands(img)

    new_img = cv2.imread('resized_test.jpg')

    if len(hands) == 2:

        if handDetector.fingersUp(hands[0]) == [1, 1, 0, 0, 0] and handDetector.fingersUp(hands[1]) == [1, 1, 0, 0, 0]:

            lmList1 = hands[0]['lmList']
            lmList2 = hands[1]['lmList']

            if distStart is None:

                length, info, img = handDetector.findDistance(hands[0]['center'], hands[1]['center'], img)
                distStart = length

            length, info, img = handDetector.findDistance(hands[0]['center'], hands[1]['center'], img)

            zoom_range = int((length - distStart) // 2)
            cx, cy = info[4:]
            print(zoom_range)

    else:
        distStart = None

    try:
        h, w, _ = new_img.shape

        newH, newW = ((h + zoom_range) // 2) * 2, ((w + zoom_range) // 2) * 2
        new_img = cv2.resize(new_img, (newW, newH))

        img[cy - newH // 2:cy + newH // 2, cx - newW // 2:cx + newW // 2] = new_img

    except:
        pass

    cv2.imshow('Virtual Zoom Gesture', img)
    cv2.waitKey(1)