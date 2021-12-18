from cvzone.HandTrackingModule import HandDetector
import cv2

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1, detectionCon=0.7)

while True:

    success, img = cap.read()
    hands, img = detector.findHands(img)

    if hands:

        hand = hands[0]
        lm_list, b_box = hand['lmList'], hand['bbox']

        fingers = detector.fingersUp(hand)

        print(fingers)


    cv2.imshow("Image", img)
    cv2.waitKey(1)