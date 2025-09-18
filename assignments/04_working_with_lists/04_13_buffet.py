menu_items = ('pizza', 'pasta', 'salad', 'soup', 'sandwich')

print("Original menu:")
for item in menu_items:
    print(item)

try:
    menu_items[0] = 'burger'
except TypeError as e:
    print(f"\nError when trying to modify tuple: {e}")

print("\nRevised menu:")
new_menu_items = ('burger', 'pasta', 'salad', 'steak', 'sandwich')
for item in new_menu_items:
    print(item)