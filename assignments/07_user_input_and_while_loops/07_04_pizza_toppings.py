print("Welcome to Python Pizza!")
print("Enter your pizza toppings one by one.")
print("Type 'quit' when you're done.")
print("=" * 40)

while True:
    topping = input("\nEnter a pizza topping: ").strip()
    
    if topping.lower() == 'quit':
        print("\nYour pizza order is complete!")
        break
    elif topping == "":
        print("Please enter a topping or 'quit' to finish.")
    else:
        print(f"  → Adding {topping.title()} to your pizza!")