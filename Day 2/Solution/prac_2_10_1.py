scores = [85, 92, 78, 90, 88, 76, 94, 89]

print("Original scores:", scores)

# Bubble sort algorithm to arrange scores in ascending order
n = len(scores)
for i in range(n - 1):
    for j in range(0, n - i - 1):
        if scores[j] > scores[j + 1]:
            # Swap the elements if they are in the wrong order
            scores[j], scores[j + 1] = scores[j + 1], scores[j]

# Display the sorted list of scores
print("Sorted scores (in ascending order):", scores)