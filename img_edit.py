import Tkinter as tk
import cv2
import tkFileDialog
import numpy as np

def main():
    img = np.zeros((480,640,3), np.uint8)
    flag = 1
    wnd = 3
    while True:
        if flag == 1:
            dst = cv2.blur(img, (wnd,wnd))
            text = "Mean blur"
        elif flag == 2:
            dst = cv2.GaussianBlur(img, (wnd,wnd),0)
            text = "Gaussian blur"
        elif flag == 3:
            dst = cv2.medianBlur(img, wnd)
            text = "Median blur"
        elif flag == 4:
            dst = cv2.bilateralFilter(img, wnd, 75,75)
            text = "Bilateral blur"
        elif flag == 5:
            mask = cv2.GaussianBlur(img, (wnd,wnd),0)
            dst=  cv2.addWeighted(img, 1.5, mask, -0.5, 0)
            text = "UnSharp mask"
        font = cv2.FONT_HERSHEY_PLAIN
        text = text+", window = "+str(wnd)
        text1 = "o - open file, s - save file"
        text2 = "+, - adjusts window size"
        text3 = "1..5 selects blur type"
        _img = np.copy(dst)
        cv2.putText(_img, text,(20,20),font,1, (255,255,255))
        cv2.putText(_img, text1, (20, 35), font, 1, (255, 255, 255))
        cv2.putText(_img, text2, (20, 50), font, 1, (255, 255, 255))
        cv2.putText(_img, text3, (20, 65), font, 1, (255, 255, 255))
        cv2.imshow("img_blur", _img)
        key = cv2.waitKey(20) &0xFF
        if key == 27:
            break
        elif key == ord('o'):
            root = tk.Tk()
            root.withdraw()
            file = tkFileDialog.askopenfilename()
            img = cv2.imread(file)
        elif key == ord('s'):
            root = tk.Tk()
            root.withdraw()
            file = tkFileDialog.asksaveasfilename()
            cv2.imwrite(file, dst)
        elif key in [ ord(c) for c in ['1','2','3','4','5']]:
            flag = key - ord('1') + 1
        elif key == ord('+'):
            wnd = wnd + 2
        elif key == ord('-'):
            wnd = max(1, wnd-2)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()