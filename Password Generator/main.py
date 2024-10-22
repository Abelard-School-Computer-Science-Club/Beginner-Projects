# RANDOM MODULE
import random
import string

# INPUT STATEMENT
length = int(input("Enter the desired password length: "))
include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
include_digits = input("Include digits? (y/n): ").lower() == 'y'
include_special = input("Include special characters? (y/n): ").lower() == 'y'

# LIST AND STRING MANIPULATION
characters = ""
if include_uppercase:
    characters += string.ascii_uppercase
if include_lowercase:
    characters += string.ascii_lowercase
if include_digits:
    characters += string.digits
if include_special:
    characters += string.punctuation

# WHILE LOOP
if characters:
    password = ''.join(random.choice(characters) for _ in range(length))  # Generate random password
    print(f"Generated Password: {password}")
else:
    print("No character types selected. Unable to generate a password.")