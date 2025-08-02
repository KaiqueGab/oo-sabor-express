# Restaurant "O Sabor"

A simple restaurant management system built in Python, allowing you to manage restaurants, menus, and customer ratings.

> **This project was developed as part of the "Python with Object-Oriented Programming" training from [Alura](https://cursos.alura.com.br/formacao-linguagem-python).**

## Features

- Register restaurants with categories
- Add beverages, dishes, and desserts to the menu
- Apply discounts to menu items
- Display restaurant menus
- Receive and calculate customer ratings

## How to Run

1. Clone this repository.
2. Make sure you have Python 3.12^ installed.
3. Run the main application:

```bash
python app.py
```

## Example Usage

```python
from models.restaurante import Restaurant
from models.menu.beverage import Beverage
from models.menu.dishes import Dishes
from models.menu.dessert import Dessert

restaurant = Restaurant('Square', 'Gourmet')
juice = Beverage('Orange Juice', 5.00, 'Medium')
salad = Dishes('Caesar Salad', 15.00, 'Salad with lettuce, croutons and Caesar dressing')
dessert = Dessert('Chocolate Brownie', 10.00, 'Small', 'Sweet', 'Chocolate brownie with ice cream')

restaurant.add_to_menu(juice)
restaurant.add_to_menu(salad)
restaurant.add_to_menu(dessert)

restaurant.show_menu
```

## Requirements

- Python >= 3.12

This project is for educational purposes.