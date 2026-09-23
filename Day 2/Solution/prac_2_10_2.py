my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# Create an empty list to store unique elements
unique_list = []

# Iterate through the original list
for item in my_list:
    # If the item is not already in the unique list, add it
    if item not in unique_list:
        unique_list.append(item)

my_list = unique_list

print("The list with unique elements only:")
print(my_list)