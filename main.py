import cv2
import numpy as np
# from PIL import Image, ImageGrey

# Return number of powercells seen by the camera
def count_powercells():
    img = Image.open("Robot_intake.jpg")
    imgG = ImageGrey.greyscale(img) 


    # Process
    # 1. Grayscale image
    # 2. Filter out HSV value of powercells
    # 3. Count the number of circles (number of powercells)


# Send the number of powercells to the robot
def networktables_send(powercell_count):
