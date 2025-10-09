# Version 1: Conditional test in while statement
print("PIZZA TOPPINGS - VERSION 1")
print("=" * 35)
print("Enter pizza toppings. Type 'stop' to finish.")

topping = ""  # Initialize the variable

while topping.lower() != "stop":
    topping = input("\nEnter a topping: ").strip()
    
    if topping.lower() != "stop" and topping != "":
        print(f"  → Adding {topping.title()} to your pizza!")

print("\nYour pizza order is complete!")