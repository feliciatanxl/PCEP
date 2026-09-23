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
print()

while True:
    print("Toggle permissions:")
    print("1. Read permission")
    print("2. Write permission")
    print("3. Execute permission")
    print("4. Delete permission")
    print("5. Exit")

    toggle_choice = int(input("Enter the number of the permission you want to toggle: "))

    # Toggle the selected permission
    if toggle_choice == 1:
        permission_bitmask ^= read_permission
    elif toggle_choice == 2:
        permission_bitmask ^= write_permission
    elif toggle_choice == 3:
        permission_bitmask ^= execute_permission
    elif toggle_choice == 4:
        permission_bitmask ^= delete_permission
    else:
        break

# Check individual permissions using bitwise operations
has_read = (permission_bitmask & read_permission) != 0
has_write = (permission_bitmask & write_permission) != 0
has_execute = (permission_bitmask & execute_permission) != 0
has_delete = (permission_bitmask & delete_permission) != 0

# Display updated permissions and the new permission bitmask
print("\nUser permissions after changes:")
print("Read permission:", has_read)
print("Write permission:", has_write)
print("Execute permission:", has_execute)
print("Delete permission:", has_delete)
print("New permission bitmask:", permission_bitmask)