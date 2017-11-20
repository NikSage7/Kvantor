# ~*~ coding: utf8 ~*~
import cv2,numpy as np
from collections import deque

if __name__ == '__main__':
    cam = cv2.VideoCapture(0)
    thresh1 = 100
    thresh2 = 200
    win =deque([])
    for i in range(10):
        win.append(np.zeros((480,640)))

    while (cam.isOpened):
        _, img = cam.read()
        edges = cv2.Canny(img,thresh1,thresh2)
        win.popleft()
        win.append(edges)
        _edges = sum(win)
        edges1 = _edges.astype(np.uint8)
        #Обноружение контуров
        contours, hierarchy = cv2.findContours(edges1,cv2.RETR_TREE,
                                               cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(img, contours,-1,(0,255,0),3)


        #Вывод на экран
        text = "thresh1 = %d, thresh2 = %d," % (thresh1,thresh2,)
        cv2.putText(edges, text, (50,50),cv2.FONT_HERSHEY_PLAIN,
                    2,(255,255,255),1)
        cv2.imshow("img",img)
        cv2.imshow("canny", _edges)
        key = cv2.waitKey(20)%0xff
        if key == 27:
            break
        if key == ord('+'):
            thresh1 = thresh1 + 10
        if key == ord('-'):
            thresh1 = max(0,thresh1-10)
        if key == ord('0'):
            thresh2 = thresh2 +10
        if key == ord('9'):
            thresh2 = max(0,thresh2-10)




