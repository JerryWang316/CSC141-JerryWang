# Example 1: Proper function naming and spacing
def calculate_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width

def calculate_perimeter(length, width):
    """Calculate the perimeter of a rectangle."""
    return 2 * (length + width)

# Example 2: Clear parameter names and proper indentation
def create_user_profile(first_name, last_name, age, location):
    """Create a dictionary with user profile information."""
    user_profile = {
        'first_name': first_name,
        'last_name': last_name,
        'age': age,
        'location': location
    }
    return user_profile

# Example 3: Proper use of default values and line length
def format_name(first_name, last_name, middle_name=''):
    """Return a formatted full name.
    
    If middle_name is provided, include it in the formatted name.
    """
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

# Using the functions
print(calculate_area(10, 5))
print(calculate_perimeter(10, 5))

user = create_user_profile('John', 'Doe', 30, 'New York')
print(user)

print(format_name('john', 'doe'))
print(format_name('john', 'doe', 'michael'))