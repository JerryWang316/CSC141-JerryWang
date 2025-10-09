# 7-9. No Pastrami
# Create a list of sandwich orders with multiple pastrami sandwiches
sandwich_orders = [
    'tuna', 
    'pastrami', 
    'turkey club', 
    'pastrami', 
    'vegetarian', 
    'ham and cheese', 
    'roast beef', 
    'pastrami', 
    'chicken salad'
]

# Create an empty list for finished sandwiches
finished_sandwiches = []

print("PYTHON DELI - ORDER PROCESSING")
print("=" * 45)

# Announce that pastrami is out of stock
print("\n ATTENTION: The deli has RUN OUT OF PASTRAMI today!")
print("We will remove all pastrami orders from your list.\n")

# Remove all occurrences of 'pastrami' from sandwich_orders
print("Removing pastrami sandwiches from orders...")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    print("  → Removed one pastrami sandwich")

print(f"\n All pastrami sandwiches removed. Remaining orders: {len(sandwich_orders)}")

# Process the remaining sandwich orders
print("\n" + "=" * 45)
print("Processing remaining orders...\n")

for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("\n" + "=" * 45)
print("ORDER COMPLETE!")
print("All sandwiches have been made.\n")

# Print a message listing each sandwich that was made
print("Sandwiches made today:")
for i, sandwich in enumerate(finished_sandwiches, 1):
    print(f"{i}. {sandwich.title()} Sandwich")