# Modified dictionary with lists of favorite numbers
favorite_numbers = {
    'Jerry': [6, 12, 18],
    'Seyeon': [5, 7],
    'Sohyun': [8, 3, 42],
    'Marie': [9, 21, 33, 47],
    'Marcello': [1]}

print("Favorite Numbers:")
print("=" * 30)

# Loop through the dictionary and print each person's favorite numbers
for name, numbers in favorite_numbers.items():
    # Format the numbers list nicely
    if len(numbers) == 1:
        numbers_str = str(numbers[0])
    else:
        # Join all but the last number with commas, then add "and" before the last number
        numbers_str = ", ".join(str(num) for num in numbers[:-1]) + f" and {numbers[-1]}"
    
    print(f"{name}: {numbers_str}")