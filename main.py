# Import OpenCV libraries
# Import NetworkTables libraries

# Return number of powercells seen by the camera
def count_powercells():
    # Process
    # 1. Grayscale image
    # 2. Filter out HSV value of powercells
    # 3. Count the number of circles (number of powercells)


# Send the number of powercells to the robot
def networktables_send(powercell_count):
