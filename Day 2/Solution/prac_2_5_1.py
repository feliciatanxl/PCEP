# Get the permission bitmask from the user
permission_bitmask = int(input("Enter the permission bitmask (integer): "))

# Define permission flags
read_permission = 1  # Bit 0
write_permission = 2  # Bit 1
execute_permission = 4  # Bit 2
delete_permission = 8  # Bit 3

# Check individual permissions using bitwise operations
has_read = (permission_bitmask & read_permission) != 0
has_write = (permission_bitmask & write_permission) != 0
has_execute = (permission_bitmask & execute_permission) != 0
has_delete = (permission_bitmask & delete_permission) != 0

# Print the results
print("User permissions:")
print("Read permission:", has_read)
print("Write permission:", has_write)
print("Execute permission:", has_execute)
print("Delete permission:", has_delete)
