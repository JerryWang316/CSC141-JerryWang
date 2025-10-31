# 9-13. Dice
import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self):
        return random.randint(1, self.sides)

# Create a 6-sided die and roll it 10 times
print("Rolling a 6-sided die 10 times:")
six_sided_die = Die()
for i in range(10):
    print(six_sided_die.roll_die(), end=" ")
print("\n")

# Create a 10-sided die and roll it 10 times
print("Rolling a 10-sided die 10 times:")
ten_sided_die = Die(10)
for i in range(10):
    print(ten_sided_die.roll_die(), end=" ")
print("\n")

# Create a 20-sided die and roll it 10 times
print("Rolling a 20-sided die 10 times:")
twenty_sided_die = Die(20)
for i in range(10):
    print(twenty_sided_die.roll_die(), end=" ")
print("\n")