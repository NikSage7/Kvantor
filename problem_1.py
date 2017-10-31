import cv2, numpy as np




def click (event,x,y,flags, param):
    global flag, shot,startx, starty, endx, endy
    if event ==cv2.EVENT_LBUTTONDOWN:
        flag = True
        startx = endx = x
        starty = endy = y
    elif event == cv2.EVENT_MOUSEMOVE and flag:
        endx = x
        endy = y
    elif event == cv2.EVENT_LBUTTONUP:
        flag = False
        shot = True



def main():
    global startx, starty, endx ,endy, flag, shot
    flag = False
    shot = False
    endx = endy = 0

    cap = cv2.VideoCapture(0)
    cv2.namedWindow("camera")
    cv2.namedWindow("region")
    cv2.setMouseCallback("camera",click)
    reg = np.zeros((200,200,1),np.uint8)

    while (cap.isOpened()):
        _, img = cap.read()
        _img =np.copy(img)

        if flag:
            cv2.rectangle(_img,(startx,starty),(endx,endy,),
                          (0,255,0),2)
        if shot:
            _ey = max(starty,endy)
            _ex = max(startx,endx)
            _sy = min(starty,endy)
            _sx = min(startx,endx)
            xs = max(1,_ex - _sx)
            ys = max(1,_ey - _sy)

            reg = img[_sy:_ey+1, _sx:_ex+1]
            reg = cv2.resize(reg,
                             (xs * 4, ys * 4), interpolation = cv2.INTER_CUBIC)
            shot = False


            reg = cv2.cvtColor(reg,cv2.COLOR_BGR2GRAY)

        wnd = 5
        kern = np.ones((wnd,wnd),np.float32)*(-1)
        kern[wnd/2,wnd/2] = wnd *wnd
        _reg =cv2.filter2D(reg,-1,kern)
        ############################################
        _,bin = cv2.threshold(_reg, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        kern = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        open = cv2.morphologyEx(bin,cv2.MORPH_OPEN, kern)
        close = cv2.morphologyEx(bin,cv2.MORPH_CLOSE, kern)
        grad = cv2.morphologyEx(cv2.bitwise_not(bin),
                                cv2.MORPH_GRADIENT,
                                kern)

        #############################################



        cv2.imshow("camera",_img)
        cv2.imshow("region",bin)
        cv2.imshow("open",open)
        cv2.imshow("close",close)
        cv2.imshow("grad",grad)
        key = cv2.waitKey(10) & 0xff
        if key == 27:

            break








if __name__ == '__main__':
   main()