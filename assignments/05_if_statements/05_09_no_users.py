print("=== VERSION 1: LIST WITH USERS ===")
usernames = ['admin', 'jaden', 'sarah', 'mike', 'jerry']

if usernames:  # Check if list is not empty
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")


print("\n=== VERSION 2: EMPTY LIST ===")
usernames = []

if usernames:  # Check if list is not empty
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")