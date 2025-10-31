# 9-16. Python Module of the Week
# This is an exploration exercise, not a coding exercise
# Visit https://pymotw.com to explore Python modules

# Example: Using the random module (which we've already been using)
import random

# Demonstrate some random module functions
print("Random module examples:")
print(f"Random float between 0 and 1: {random.random()}")
print(f"Random integer between 1 and 100: {random.randint(1, 100)}")
print(f"Random choice from a list: {random.choice(['apple', 'banana', 'cherry'])}")

# Shuffle a list
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(f"Shuffled list: {my_list}")