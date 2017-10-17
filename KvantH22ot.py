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
        contours, hierarchy = cv2.findContours(
            mask,
            cv2.RETR_TREE,
            cv2.CHAIN_APPROX_SIMPLE
        )
        centers = []
        for cnt in contours:
            M = cv2.moments(cnt)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/ M['m00'])
            centers.append((cx,cy))

        cv2.drawContours(
            img,
            contours,
            -1,
            (0, 0, 255),
            2

            )
        for center in centers:
            cv2.circle(img,center,
                       3, (255, 0, 0),-1)
            cv2.putText(img, "Green", center,
                        cv2.FONT_HERSHEY_PLAIN,
                        2, (0,0,0))


        cv2.imshow("win", img)
        cv2.imshow("mask", res)
        key = cv2.waitKey(20) & 0xff
        if key == 27:
           break








if __name__ == '__main__':
    main()