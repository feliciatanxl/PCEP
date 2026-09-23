# Get two positive integers from the user
num1 = int(input("Enter the first positive integer: "))
num2 = int(input("Enter the second positive integer: "))

# Initialize variables
result = 0
bit_position = 0

# Store the original value of num1
original_num1 = num1

# Calculate the product using bit shifting
while num1 > 0:
    # Check if the least significant bit of num1 is 1
    if num1 & 1:
        # Left-shift num2 by bit_position and add to result
        result += (num2 << bit_position)
    # Right-shift num1 to process the next bit
    num1 >>= 1
    bit_position += 1

# Print the product
print("The product of", original_num1, "and", num2, "is:", result)