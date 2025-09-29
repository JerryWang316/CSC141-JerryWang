# List of usernames including 'admin'
usernames = ['admin', 'jaden', 'sarah', 'mike', 'jerry']

print("=== USER GREETINGS ===")

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username.title()}, thank you for logging in again.")