pizzas = ['Cheese', 'Pepperoni and Sausage', 'Veggie Delite', 'Barbeque Chicken']
friend_pizzas = pizzas.copy()

pizzas.append('Hawaiian')
friend_pizzas.append('Supreme')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(f"- {pizza}")

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"- {pizza}")