# Test code
# Import OpenCV libraries
# Import NetworkTables libraries
import numpy as np
import cv2

# Return of powercells seen by the camera
def count_powercells(frame1, frame2):

    hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)

    # Lower and upper HSV values from OpenSight
    l_h, l_s, l_v = 0, 80, 72
    u_h, u_s, u_v = 27, 218, 219

    #this converts the image into an array
    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    #The rest of the code below is filtering the image
    mask = cv2.inRange(hsv, l_b, u_b)
    kernel = np.ones((2, 2), np.uint8)
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    res = cv2.bitwise_and(frame1, frame1, mask=opening)

    diff = cv2.absdiff(res, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return len(contours)

def powercell_countors(frame):
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Powercell HSV values
    lower = np.array([10, 45, 89])
    upper = np.array([52, 218, 219])

    # Threshold the HSV image to get only powercells
    mask = cv.inRange(hsv, lower, upper)

    ret, thresh = cv.threshold(mask, 127, 255, 0)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # Drawing the countors on an output image
    # Saving the processed image file
    # 1. Draw countours on the image (https://docs.opencv.org/master/d4/d73/tutorial_py_contours_begin.html)
    # 2. Save the image with the countours drawn (https://www.tutorialkart.com/opencv/python/opencv-python-save-image-example/)
