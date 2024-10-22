# RANDOM MODULE
import random

# LIST AND STRING MANIPULATION
words = [
    "water", "brother", "marker", "apple", "banana", "orange", "grape",
    "strawberry", "kiwi", "melon", "peach", "pear", "plum", "cherry",
    "pineapple", "coconut", "mango", "papaya", "apricot", "blueberry",
    "blackberry", "raspberry", "pomegranate", "cucumber", "carrot",
    "broccoli", "spinach", "lettuce", "tomato", "potato", "onion",
    "garlic", "ginger", "pepper", "zucchini", "eggplant", "squash",
    "pumpkin", "beet", "turnip", "radish", "celery", "parsley",
    "basil", "oregano", "cilantro", "thyme", "rosemary", "sage",
    "cinnamon", "nutmeg", "vanilla", "honey", "sugar", "salt",
    "pepper", "coffee", "tea", "milk", "cream", "butter",
    "cheese", "yogurt", "bread", "cake", "cookie", "brownie",
    "icecream", "candy", "chocolate", "soda", "juice", "smoothie",
    "soup", "salad", "pasta", "rice", "noodle", "pizza",
    "sandwich", "taco", "burger", "hotdog", "seafood", "steak",
    "chicken", "beef", "pork", "lamb", "fish", "shellfish",
    "tofu", "quinoa", "beans", "lentils", "nuts", "seeds",
    "grains", "flour", "corn", "oats", "barley", "rye"
]

answer = random.choice(words)
hidden = ["_" for i in range(len(answer))]

# INPUT STATEMENT
attempts = 6 
flag = True

# WHILE LOOP
while flag:
    print(attempts)
    guess = input("Guess your letter: ")

    # CHECKING GUESSES
    for i in range(len(answer)):
        if guess == answer[i]:
            hidden[i] = guess

    print(" ".join(hidden))

    if guess not in answer:
        attempts -= 1
        
    if "".join(hidden) == answer:
        flag = False
        print("You Won!") 

    # CHECKING FOR LOSING CONDITION
    if attempts == 0:
        flag = False
        print("You Lost!") 