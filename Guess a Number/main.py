# 🤔🔢 Guess a Number!

import random

_min = 1
_max = 10

secret_num = random.randint(_min, _max) # 🤐 Set any number you like!

for i in range(5):

    print("-" * 50, f"\nAttempts remaining({i+1}/5)")

    # Ask user for input
    guess = int(input(f"🤔Guess a number between {_min} to {_max}: "))

    # ✅ Check Input
    if guess > _max or guess < _min:
         print(f"⛔ Incorrect guess. Guess between {_min} and {_max}.")

    # 👀 Check results

    elif guess == secret_num:
        print("🥳 Correct! You guessed the number!")
        break

    elif guess > secret_num:
        print("❌ You guessed too high! Try again!")

    else:
        print("❌ You guessed too low! Try again!")
