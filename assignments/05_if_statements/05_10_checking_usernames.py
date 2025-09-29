# List of current usernames
current_users = ['john', 'sarah', 'admin', 'mike', 'jerry', 'David']

# List of new usernames to check (some duplicates with different cases)
new_users = ['JOHN', 'sarah', 'alex', 'Maria', 'david', 'Sophie']

print("=== USERNAME AVAILABILITY CHECK ===")
print(f"Current users: {current_users}")
print(f"New users to check: {new_users}")
print()

# Create a copy of current_users in lowercase for case-insensitive comparison
current_users_lower = [user.lower() for user in current_users]

# Loop through new_users and check for availability
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, the username '{new_user}' is already taken. Please enter a new username.")
    else:
        print(f"Congratulations! The username '{new_user}' is available!")