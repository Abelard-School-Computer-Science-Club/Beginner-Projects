# RANDOM MODULE
import random

# INPUT STATEMENT
number_of_dice = int(input("Enter the number of dice you want: "))

# FOR LOOP
counter = 0
for i in range(number_of_dice):
    dice_roll = random.randint(1, 6)
    counter += 1
    print("Dice #" + str(counter) + ", Value: " + str(dice_roll))