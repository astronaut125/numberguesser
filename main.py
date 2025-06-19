#evil computer program thingie

import random

print("Welcome to ur doom >:)")
print("You have 7 tries or else")

low = int(input("Enter the lowest possible number for ur doom :) "))
high = int(input("Enter the highest possible number for more doom cuz i said so "))

print(f"\nYou have 7 chances to guess the correct number between {low} and {high} or ummmm ig I will eat u or something")

num = random.randint(low, high)

maxguesses = 7
currentguesses = 0

#loops until current guesses are equal to max guesses

while currentguesses < maxguesses: 
    currentguesses+=1
    guess=int(input("Decision time mwahahaha im evil "))
    
    if guess == num:
        print("*evil computer dies*")
        break
    elif currentguesses >= maxguesses and guess != num:
        print(f"HA you fool the real answer was {num} you will now explode or ummmm I will eat you? idk yet just get in the basement")
    elif guess > num:
        print("try lower or you'll live in my basement that computers may or may not have not sure yet")
    elif guess < num:
        print("guess higher or ummm idk figure out ur own demise im lazy")


