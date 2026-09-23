income = float(input("Enter the annual income: "))

tax = 0.0

if income > 85528:
    tax = (income - 85528) * .32 + 14839.2
else:
    tax = income * .18 - 556.2

if tax < 0:
    tax = 0.0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")
