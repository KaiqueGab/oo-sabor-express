# Restaurant "O Sabor"

A simple restaurant management system built in Python, allowing you to manage restaurants, menus, and customer ratings.

## Features

- Register restaurants with categories
- Add beverages, dishes, and desserts to the menu
- Apply discounts to menu items
- Display restaurant menus
- Receive and calculate customer ratings
<!-- ## Project Structure -->

<!-- ```
restaurante_o_sabor/
│
├── app.py                  # Main application file
├── models/
│   ├── restaurante.py      # Restaurant class
│   ├── rating.py           # Rating class
│   └── menu/
│       ├── item_menu.py    # Abstract base class for menu items
│       ├── beverage.py     # Beverage class
│       ├── dishes.py       # Dishes class
│       └── dessert.py      # Dessert class
└── README.md               # Project documentation
``` -->
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