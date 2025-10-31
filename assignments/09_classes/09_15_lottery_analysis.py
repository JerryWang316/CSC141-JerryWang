# 9-15. Lottery Analysis
import random

# Create the lottery pool
lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Define my ticket
my_ticket = [7, 'A', 3, 'D']

# Counter for number of attempts
attempts = 0

# Keep trying until we win
while True:
    attempts += 1
    # Draw a winning combination
    winning_combo = random.sample(lottery_pool, 4)
    
    # Check if my ticket matches the winning combination
    # We need to sort both to compare regardless of order
    if sorted(my_ticket) == sorted(winning_combo):
        print(f"Congratulations! You won after {attempts} attempts!")
        print(f"Your ticket: {my_ticket}")
        print(f"Winning combination: {winning_combo}")
        break
    
    # Optional: print progress every 100,000 attempts
    if attempts % 100000 == 0:
        print(f"Still trying... {attempts} attempts so far")