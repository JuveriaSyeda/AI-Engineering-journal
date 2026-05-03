import random

# Guessing Game
n = random.randint(1,100)
attempts = 0

while attempts < 5:
    # user Input
    x = int(input("Enter you guess number: "))
    #incrementing attempts
    attempts += 1
    print(f"You are only left with {5-attempts}")
    # condition where the guess number is high or low

    if x > n:
        print("Too High")
    elif x < n:
        print('Too low')
    else:
        print("Correct")
        break
print("You have completed your guess")