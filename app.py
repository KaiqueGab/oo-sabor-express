from models.restaurante import Restaurant
from models.menu.beverage import Beverage
from models.menu.dishes import Dishes
from models.menu.dessert import Dessert
from models.rating import Rating

restaurant_square = Restaurant('Square', 'Gourmet')
restaurant_pepper = Restaurant('Pepper', 'Fast Food')

beverage_juice = Beverage('Orange Juice', 5.00, 'Medium')
beverage_juice.apply_discount()

salad_dish = Dishes('Caesar Salad', 15.00, 'Salad with lettuce, croutons and Caesar dressing')
salad_dish.apply_discount()

chocolate_dessert = Dessert('Chocolate Brownie', 10.00, 'Small', 'Sweet', 'Chocolate brownie with ice cream')
chocolate_dessert.apply_discount()

restaurant_square.add_to_menu(beverage_juice)
restaurant_square.add_to_menu(salad_dish)
restaurant_square.add_to_menu(chocolate_dessert)

restaurant_pepper.toggle_status()

restaurant_square.receive_rating('Alice', 4.5)
restaurant_pepper.receive_rating('Bob', 3.0)

def main():
    restaurant_square.list_restaurants()
    print('\n')
    restaurant_square.display_menu
    print('\n')
    restaurant_pepper.display_menu

if __name__ == "__main__":
    main()