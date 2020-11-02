# Import OpenCV libraries
# Import NetworkTables libraries
from networktables import NetworkTables

def main():
    # Setup NetworkTables

    while count_powercells() != -1:
        # Count the powercells

        # Send the data through NetworkTables


# Return of powercells seen by the camera
def count_powercells():


# Send the number of powercells to the robot
def networktables_send(vision_table, powercell_count):
    vision_table.putNumber("powercell_count", powercell_count)

# Setup NetworkTables
def networktables_setup():
    NetworkTables.initialize()
    vision_table = NetworkTables.getTable("intake-vision")
    return vision_table