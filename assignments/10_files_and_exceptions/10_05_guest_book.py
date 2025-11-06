# 10-5. Guest Book
print("Welcome to the Guest Book!")
print("Enter 'quit' to finish adding names.")

with open('guest_book.txt', 'w') as file:
    while True:
        name = input("Please enter your name: ")
        
        if name.lower() == 'quit':
            break
        
        file.write(f"{name}\n")
        print(f"Thank you, {name}. You have been added to the guest book.")

print("\nAll guest names have been saved to guest_book.txt")