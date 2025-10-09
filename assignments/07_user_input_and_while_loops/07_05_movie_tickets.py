# Movie Tickets program
print("WELCOME TO PYTHON CINEMA")
print("=" * 35)
print("Ticket Prices:")
print("• Under 3: FREE")
print("• 3-12 years: $10")
print("• Over 12: $15")
print("=" * 35)

while True:
    age_input = input("\nEnter your age (or 'quit' to exit): ").strip()
    
    # Check if user wants to quit
    if age_input.lower() == 'quit':
        print("Thank you for visiting Python Cinema!")
        break
    
    try:
        age = int(age_input)
        
        if age < 0:
            print("Please enter a valid age.")
        elif age < 3:
            print("Your ticket is FREE!")
        elif age <= 12:
            print("Your ticket costs $10.")
        else:
            print("Your ticket costs $15.")
            
    except ValueError:
        print("Please enter a valid age or 'quit' to exit.")