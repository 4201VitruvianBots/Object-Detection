from PIL import Image, ImageDraw
import numpy as np
from math import sqrt
import cv2
# from PIL import Image, ImageGrey

# Return number of powercells seen by the camera
#def count_powercells():

# Open camera stream
# Look at opencv_python_object_detection.py lines 8-13 for how to open and read a camera stream
    

def find_circles():
    # Change this line so the image is read by the camera
    # img = cv2.imread('edge.png',0)
    img = cap.read('edge.png',0)

    # The lines below should be fine
    # Make sure you have the correct filtering code though
    # Look at opencv_python_object_detection.py lines 70 - 86
 
    
    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

  
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
  





    # Lines 21 through 29 are not needed since you don't need to show the circles
    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),1)
        # draw the center of the circle
        cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),1)

        cv2.imshow('detected circles',cimg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


    # Process
    # 1. Grayscale image
    # 2. Filter out HSV value of powercells
    # 3. Count the number of circles (number of powercells)


# Send the number of powercells to the robot
#def networktables_send(powercell_count):
