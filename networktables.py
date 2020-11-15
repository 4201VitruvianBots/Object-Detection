from networkTables import NetworkTables

def networktables_send(vision_table, powercell_count):
    vision_table.putNumber("powercell_count", powercell_count)

def networktables_setup():
    NetworkTables.initialize(server="roborio-4201-frc.local")
    vision_table = NetworkTables.getTable("intake-vision")
    return vision_table