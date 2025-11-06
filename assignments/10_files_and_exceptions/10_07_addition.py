# 10-7. Addition Calculator
print("Enter 'q' at any time to quit.")

while True:
    try:
        num1 = input("\nEnter the first number: ")
        if num1.lower() == 'q':
            break
            
        num2 = input("Enter the second number: ")
        if num2.lower() == 'q':
            break
            
        result = int(num1) + int(num2)
        print(f"The sum of {num1} and {num2} is {result}")
        
    except ValueError:
        print("Error: Please enter valid numbers, not text!")