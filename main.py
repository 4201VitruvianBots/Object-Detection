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

def networktables_send(vision_table, powercell_count):
    vision_table.putNumber("powercell_count", powercell_count)

def networktables_setup():
    NetworkTables.initialize()
    vision_table = NetworkTables.getTable("intake-vision")
    return vision_table