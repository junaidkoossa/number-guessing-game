import random

secret = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Your guess: "))
    attempts += 1  
    
    if guess > secret:
        print("Too high! Try again.")

    elif guess < secret:
        print("Too low! Try again.")

    else:
        print(f"Congratulations! You found it in {attempts} attempts!")
        break