# 9-2. Three Restaurants
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

restaurant1 = Restaurant("Burger King", "Fast Food")
restaurant2 = Restaurant("Sushi Zen", "Japanese")
restaurant3 = Restaurant("Taco Fiesta", "Mexican")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()