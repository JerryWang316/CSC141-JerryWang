print("=== Testing all alien colors ===")

# Test with green alien (should pass)
alien_color = 'green'
print(f"Alien color: {alien_color}")
if alien_color == 'green':
    print("You just earned 5 points!")
print()

# Test with yellow alien (should fail)
alien_color = 'yellow'
print(f"Alien color: {alien_color}")
if alien_color == 'green':
    print("You just earned 5 points!")
print()

# Test with red alien (should fail)
alien_color = 'red'
print(f"Alien color: {alien_color}")
if alien_color == 'green':
    print("You just earned 5 points!")

# Testing all three colors in sequence
alien_colors = ['green', 'yellow', 'red']

for color in alien_colors:
    print(f"Testing alien color: {color}")
    if color == 'green':
        print("You just earned 5 points!")
    print("---")