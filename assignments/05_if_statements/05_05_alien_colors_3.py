# Test all three colors in sequence
alien_colors = ['green', 'yellow', 'red']

for color in alien_colors:
    print(f"\nAlien color: {color}")
    if color == 'green':
        print("You just earned 5 points!")
    elif color == 'yellow':
        print("You just earned 10 points!")
    else:
        print("You just earned 15 points!")