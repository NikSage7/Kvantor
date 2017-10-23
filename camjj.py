import cv2, numpy as np
import os


def click(event, x ,y, flags, param):
    global points

    if event ==cv2.EVENT_LBUTTONDOWN:
        if len(points) <3:
            points.append((x,y))
        else:
            points = []


def main():
    global points
    points = []
    cap0 = cv2.VideoCapture(0)
    cap = cv2.VideoCapture(1)
    angle = 0
    scale = 0.5
    increment = 0.01
    color = 0
    oldimg = np.zeros((480, 640, 3), np.uint8)
    cv2.namedWindow("img2")
    cv2.namedWindow("img", cv2.WND_PROP_FULLSCREEN)

    cv2.setMouseCallback("img2", click)
    dat = np.zeros((480, 640, 3), np.uint8)
    while cap.isOpened():
        _, img = cap.read()
        rows, cols, channels = img.shape
        _, img2 = cap0.read()



        for point in points:
            cv2.circle(img2, point, 2 , (0,255,0))
        if len(points) == 3:
            pts1 = np.float32([0,0], [0,480],[640,0])
            pts2 = np.float32([0], points[1], points[2])

            M = cv2.warpAffineTransform(pts1, pts2)
            img2 = img2 + dst



        cv2.imshow("img2",img2)
        cv2.imshow("img", img)

        angle = angle + 7 % 360
        scale = scale + increment
        if (scale >= 1.5) or (scale <= 0.5):
            increment = -increment
        key = cv2.waitKey(20) & 0xff
        if key == 27:
            break










if __name__ == '__main__':

  main()

