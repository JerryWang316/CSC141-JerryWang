# 10-4. Guest
name = input("Please enter your name: ")

with open('guest.txt', 'w') as file:
    file.write(name)

print(f"Thank you, {name}. Your name has been recorded in guest.txt")