# 10-6. Addition
try:
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    
    result = int(num1) + int(num2)
    print(f"The sum of {num1} and {num2} is {result}")
except ValueError:
    print("Error: Please enter valid numbers, not text!")