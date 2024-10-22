# Project Description
This script chooses a random number between 1 and 100.
The player then has to guess the number.
The script tells you whether your guess is too high or too low.

# Coding The Project
We want to make it so that the user is prompted to enter an integer until their guess is correct.
We also want the program to choose a random number on it's own.
In order to do this, we will need to use the following concepts:
- **While Loop**: This will be the game loop. It will ensure that the user is prompted until they're right.
- **Input Statement**: We will need to recieve user input in order for the program to work.
- **Random Module**: This will be used to choose a random number `random.randint(lower bound, upper bound)`
- **If Statement**: This will be used in order to compare the user's guess to the chosen integer.

Altogether, once all of these concepts are applied correctly, we will have a working number guessing game.

# Dependencies
- **random** module (comes with Python, so no installation is required)