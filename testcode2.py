# What is this code used for?
import cv2
import numpy as np
#https://pythonprogramming.net/color-filter-python-opencv-tutorial/
def Prototype2():
    cap = cv2.VideoCapture(0)

    while(1):
        _, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
        lower_yellow = np.array([204,186,25])
        upper_yellow = np.array([255, 232, 31])
    
        mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
        res = cv2.bitwise_and(frame,frame, mask= mask)

        cv2.imshow('frame',frame)
        cv2.imshow('mask',mask)
        cv2.imshow('res',res)
    
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

    cv2.destroyAllWindows()
    cap.release()