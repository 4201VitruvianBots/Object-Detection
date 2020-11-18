# Import OpenCV libraries
# Import NetworkTables libraries
import cv2
import numpy as np
# Return of powercells seen by the camera

# Not sure what this function is for
def nothing(x):
    pass

 # Open our video capture source (camera)
 cap = cv2.VideoCapture(0);

 # Read frame from capture source
 ret, frame1 = cap.read()
 ret, frame2 = cap.read()
 while cap.isOpened():

  frame = cv2.imread('smarties.png')
  _, frame = cap.read()

 # Convert frame to black and while
 hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
 # Convert image into an array so it's easier to work with
 l_b = np.array([l_h, l_s, l_v])
 u_b = np.array([u_h, u_s, u_v])

 # Filter the image
 mask = cv2.inRange(hsv, l_b, u_b)
 kernel = np.ones((2, 2), np.uint8)
 opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
 res = cv2.bitwise_and(frame1, frame1, mask=opening)

 # Do some more filtering
 diff = cv2.absdiff(res, frame2)
 gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
 blur = cv2.GaussianBlur(gray, (5, 5), 0)
 _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
 dilated = cv2.dilate(thresh, None, iterations=3)
 contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cap.release()
# cv2.destroyAllWindows() Not needed
def count_powercells():
    # img = cv2.imread('edge.png',0)
    #Opened Camera stream and added code to read the frames from the camera
    cap = cv2.Videocapture
    img = cap.read('smarties.png',0)
    ret, frame1 = cap.read()
    ret, frame2 = cap.read()

    # The lines below should be fine
    # Make sure you have the correct filtering code though
    # Look at opencv_python_object_detection.py lines 70 - 86
 
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


# Send the number of powercells to the robot
#def networktables_send(powercell_count):


# Send the number of powercells to the robot
def networktables_send(powercell_count):
