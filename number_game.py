"""A very simple number guessing game, mostly for me to try out GitHub."""

import random

min = 1
max = 100
max_tries = 10

solution = random.randint(min, max)
tries = 0
guess = min - 1     # anything different from solution

print("I chose a number between", min, "and", max)
while guess != solution and tries < max_tries:
    while True:
        try:
            guess = int(input("How much? "))
            break
        except ValueError:
            print("Please type an integer")
    if guess < solution:
        print("Too small")
    if guess > solution:
        print("Too big")
    tries += 1

if guess == solution:
    print("Bravo! You found it in", tries, "tries")
else:
    print("I was thinking of", solution)
