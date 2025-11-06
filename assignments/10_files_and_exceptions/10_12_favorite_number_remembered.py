# 10-12. Favorite Number Remembered
import json

def get_stored_favorite_number():
    """Get stored favorite number if available."""
    try:
        with open('favorite_number.json') as file:
            favorite_number = json.load(file)
    except FileNotFoundError:
        return None
    else:
        return favorite_number

def get_new_favorite_number():
    """Prompt for a new favorite number."""
    favorite_number = input("What is your favorite number? ")
    with open('favorite_number.json', 'w') as file:
        json.dump(favorite_number, file)
    return favorite_number

def favorite_number_program():
    """Main program that remembers favorite number."""
    favorite_number = get_stored_favorite_number()
    
    if favorite_number:
        print(f"I know your favorite number! It's {favorite_number}.")
    else:
        favorite_number = get_new_favorite_number()
        print(f"We'll remember your favorite number, {favorite_number}!")

# Run the program
favorite_number_program()