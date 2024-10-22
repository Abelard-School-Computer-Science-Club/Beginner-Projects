# RANDOM MODULE
import random
random_int = random.randint(1, 100) #  Generating a random integer between 1 and 100

# WHILE LOOP
keep_playing = True # We will use a flag to determine whether the loop should end
while keep_playing:
    # INPUT STATEMENT
    guess = int(input("Enter your guess: "))

    # IF STATEMENT
    if guess < random_int:
        print("Too low")
    elif guess > random_int:
        print("Too high")
    else:
        print("You have guessed correctly")
        keep_playing = False # Changing flag to be False in order to break the loop