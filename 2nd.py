import random

while True:
    user = input("Roll a dice? (y/n): ").lower()

    if user == "y":
        dice = random.randint(1, 6)
        print(f"You rolled: {dice}")
    elif user == "n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid input. Please enter y or n.")