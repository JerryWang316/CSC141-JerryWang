# 9-14. Lottery
import random

# Create a list with 10 numbers and 5 letters
lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Randomly select 4 items from the pool
winning_combo = random.sample(lottery_pool, 4)

print("Lottery Results:")
print("Any ticket matching these 4 items wins a prize:")
print(winning_combo)