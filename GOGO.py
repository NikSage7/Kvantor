import cv2, numpy as np
import os

def main():
    cap = cv2.VideoCapture(0)
    angle = 0
    scale = 0.5
    increment = 0.05
    color = 0
    while cap.isOpened():
        _, img = cap.read()
        rows, cols,channels = img.shape


        M = cv2.getRotationMatrix2D((cols/2, rows/2),angle, scale)
        img = cv2.warpAffine(img,M, (cols, rows))
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        hsv[:, :, 0] = color
        color = (color + 10) & 180
        img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

        cv2.imshow("img",
                 img)
        angle = angle + 6 % 360
        scale = scale + increment
        if (scale >=1.5) or (scale <=0.5):
            increment = -increment
        key = cv2.waitKey(20) & 0xff
        if key == 27:
            break










if __name__ == '__main__':

  main()

