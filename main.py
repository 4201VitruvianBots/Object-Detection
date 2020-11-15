# Import OpenCV libraries
# Import NetworkTables libraries
from networktables import NetworkTables

def main():
    # Setup NetworkTables
    vision_table = networktables_setup()
    
    while count_powercells() != -1:
        # Count the powercells
        count = count_powercells()

        # Send the data through NetworkTables
        networktables_send(vision_table, count)