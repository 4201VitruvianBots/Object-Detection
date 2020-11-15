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
    # img = cap.read()
    img = cv2.imread('edge.png',0)

    # The lines below should be fine
    # Make sure you have the correct filtering code though
    # Look at opencv_python_object_detection.py lines 70 - 86
    cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,5,
                            param1=118,param2=8,minRadius=0,maxRadius=7)

    circles = np.uint16(np.around(circles))

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
