# Total cost of air tickets: 5 people * $450
print("Total cost of air tickets:", 450 * 5)

# Hotel expenses for five days: 2 rooms * $120 * 5 nights
print("Hotel expenses for five days:", 2 * 120 * 5)

# Total cost of the trip: air tickets + hotel + total food
print("Total cost of the trip:", (450 * 5) + (2 * 120 * 5) + 1050)

# Food expenses for each day: $1050 total food / 5 days
print("Food expenses for each day:", 1050 / 5)

# Hotel expenses incurred by the 4 friends:
# Room 1 (3 friends): fully paid by them = 120 * 5
# Room 2 (1 friend + you): split in half = (120 * 5) / 2
print("Hotel expenses incurred by the four friends:", (120 * 5) + ((120 * 5) / 2))

# The total amount your friends have to pay you:
# Their air tickets (4 * 450) + their hotel (600 + 300) + their food share (1050 * 4 / 5)
print("The total amount your friends have to pay you:", (4 * 450) + ((120 * 5) + ((120 * 5) / 2)) + (1050 * 4 / 5))