group_size = input("How many people are in your dinner group? ")

group_size = int(group_size)

if group_size > 8:
    print("I'm sorry, but you'll have to wait for a table.")
else:
    print("Your table is ready!")