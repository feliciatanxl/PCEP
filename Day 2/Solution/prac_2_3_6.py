blocks = int(input("Enter the number of blocks: "))

# Write your code here.
height = 0
no_of_layer = 1
while no_of_layer <= blocks:
    height += 1
    blocks -= no_of_layer
    no_of_layer += 1

print("The height of the pyramid:", height)