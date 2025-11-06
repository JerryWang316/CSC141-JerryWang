# 10-11. Favorite Number
import json

# Part 1: Write favorite number to file
favorite_number = input("What is your favorite number? ")

with open('favorite_number.json', 'w') as file:
    json.dump(favorite_number, file)

print("Your favorite number has been saved!")

# Part 2: Read favorite number from file
with open('favorite_number.json') as file:
    favorite_number = json.load(file)

print(f"I know your favorite number! It's {favorite_number}.")