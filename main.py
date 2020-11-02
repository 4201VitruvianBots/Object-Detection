# Import OpenCV libraries
# Import NetworkTables libraries
from networktables import NetworkTables

def main():
    # Setup NetworkTables
def networktables_setup():
    NetworkTables.initialize()
    vision_table = NetworkTables.getTable("intake-vision")
    return vision_table
    
    while count_powercells() != -1:
        # Count the powercells
    def count_powercells():

        # Send the data through NetworkTables
def networktables_send(vision_table, powercell_count):
    vision_table.putNumber("powercell_count", powercell_count)


# Return of powercells seen by the camera
def networktables_return():
    return powercell







