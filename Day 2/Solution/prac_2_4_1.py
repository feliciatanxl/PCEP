age = int(input("Enter your age: "))

# Check eligibility using logical operators
if age >= 18 and age <= 65:
    print("You are eligible to play the game!")
elif age < 18:
    print("You are not eligible to play the game. You are too young.")
else:
    print("You are not eligible to play the game. You are too old.")