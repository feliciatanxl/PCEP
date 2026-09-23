# Set the predetermined password
correct_password = "secret_password"

# Initialize the number of attempts
attempts_left = 3

print("Welcome to the Password Guessing Game!\n")
print(f"You have {attempts_left} attempts to guess the password.\n")

while attempts_left > 0:
    user_guess = input("Enter your guess: ")

    if user_guess == correct_password:
        print("Congratulations! You guessed the correct password.")
        print("You win!")
        break
    else:
        attempts_left -= 1
        if attempts_left > 0:
            print(f"Incorrect guess. You have {attempts_left} attempts left.\n")
        else:
            print("Incorrect guess. You've used all your attempts.")
            print(f"You lose. The correct password was \"{correct_password}.\"")
else:
    print("You've used all your attempts. You lose.")
