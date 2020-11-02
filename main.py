# Import OpenCV libraries
# Import NetworkTables libraries

# Return of powercells seen by the camera
def count_powercells():


# Send the number of powercells to the robot
networktablesetup 
def networktables_send(powercell_count):
    vision_table.putNumber("powercell_count", powercell_count)  
