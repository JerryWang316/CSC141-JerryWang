# 10-14. Verify User
import json

def get_stored_username():
    """Get stored username if available."""
    try:
        with open('username.json') as file:
            username = json.load(file)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    with open('username.json', 'w') as file:
        json.dump(username, file)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    
    if username:
        correct = input(f"Is {username} the correct username? (y/n) ")
        if correct.lower() == 'y':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

# Run the program
greet_user()