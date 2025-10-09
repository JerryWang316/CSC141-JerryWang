# Create a list of sandwich orders
sandwich_orders = ['tuna', 'turkey club', 'vegetarian', 'ham and cheese', 'roast beef', 'chicken salad']

# Create an empty list for finished sandwiches
finished_sandwiches = []

print("WELCOME TO THE PYTHON DELI")
print("=" * 40)

# Loop through sandwich orders and make each one
print("Processing sandwich orders...\n")

for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("\n" + "=" * 40)
print("ORDER COMPLETE!")
print("All sandwiches have been made.\n")

# Print a message listing each sandwich that was made
print("Sandwiches made today:")
for i, sandwich in enumerate(finished_sandwiches, 1):
    print(f"{i}. {sandwich.title()} Sandwich")