import random

secret = random.randint(1, 100)

while True:
    guess = int(input("Your guess: "))
    if guess > secret:
        print("Too high! Try again.")

    elif guess < secret:
        print("Too low! Try again.")

    else:
        print("Congratulations! You found it!")
        break