#this is my first number guessing game

import random

# definig variables

n = random.randint(1,99)
guess = int(input("Enter an integer from 1 to 99 "))
#do a loop

while n != "guess":
    print
    if guess < n:
        print ("Your guess is low")
        guess = int(input("Enter an integer from 1 to 99 "))
    elif guess > n:
        print("guess is high")
        guess = int(input("Enter an integer from 1 to 99 "))
    else:
        print("You guessed it")
        break
    print

    
