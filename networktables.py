from networkTables import NetworkTables

# Setup NetworkTables
NetworkTables.initialize()
vision_table = NetworkTables.getTable("intake-vision")

# Send value through NetworkTables
vision_table.putNumber("powercell_count", number)