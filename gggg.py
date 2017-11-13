import cv2
import numpy as np
import os


def main ():
    a=0
    cap = cv2.VideoCapture(0)
    while (cap.isOpened()):
        _, img = cap.read()
        kern = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        lower_green = np.array ([40,40,50])
        upper_green = np.array ([90,255,255])
        mask= cv2.inRange(
            hsv,
            lower_green,
            upper_green,

        )
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN,kern)
        res = cv2.bitwise_and(
            img,
            img,
            mask = mask
        )
        cv2.imshow("win", img)
        cv2.imshow("mask", res)
        key = cv2.waitKey(20) & 0xff
        if key == 27:
           break








if __name__ == '__main__':
    main()