# Restaurant "O Sabor"

A simple restaurant management system built in Python, allowing you to manage restaurants, menus, discounts, and customer ratings.

> **This project was developed as part of the "Python with Object-Oriented Programming" training from [Alura](https://cursos.alura.com.br/formacao-linguagem-python).**

## Features

- Register restaurants with categories
- Add beverages, dishes, and desserts to the menu
- Apply discounts to menu items
- Display restaurant menus
- Receive and calculate customer ratings
- Modular structure with classes for restaurant, rating, and menu items
- Import real menus via JSON files in the [`api/`](api/) folder
- Easily extendable for new menu item types

## Project Structure

- **app.py**: Main application file.
- **api/**: Scripts and JSON files with real restaurant menus.
- **models/**: Main system classes.
    - **restaurante.py**: Restaurant class.
    - **rating.py**: Rating class.
    - **menu/**: Menu item classes (beverage, dishes, dessert).

## How to Run

1. Clone this repository.
2. Make sure you have Python 3.12 or higher installed.
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the main application:
    ```bash
    python app.py
    ```

## Example Usage

```python
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


restaurant_square.list_restaurants()
print('\n')
restaurant_square.display_menu
print('\n')
restaurant_pepper.display_menu
```

## Requirements

- Python >= 3.12

This project is for educational purposes.