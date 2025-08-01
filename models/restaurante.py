from models.rating import Rating
from models.menu.item_menu import ItemMenu

class Restaurant:
    restaurants = []

    def __init__(self, name, category):
        """
        Initializes a Restaurant instance.

        Parameters:
        - name (str): The name of the restaurant.
        - category (str): The category of the restaurant.
        """
        self._name = name.title()
        self._category = category.upper()
        self._active = False  # Restaurant starts inactive
        self._ratings = []    # List of received ratings
        self._menu = []
        Restaurant.restaurants.append(self) # Adds the restaurant to the list

    def __str__(self):
        """Returns a string representation of the restaurant."""
        return f'{self._name} | {self._category}'

    @classmethod
    def list_restaurants(cls):
        """Displays a formatted list of all restaurants."""
        print(f'{"Restaurant Name".ljust(25)} | {"Category".ljust(25)} | {"Rating".ljust(25)} | {"Status"}')
        for restaurant in cls.restaurants:
            print(f'{restaurant._name.ljust(25)} | {restaurant._category.ljust(25)} | {str(restaurant.average_rating).ljust(25)} | {restaurant.active}')

    def toggle_status(self):
        """Toggles the active status of the restaurant."""
        self._active = not self._active

    @property
    def active(self):
        """Returns a symbol indicating the active status of the restaurant."""
        return '☑' if self._active else '☐'
    
    def receive_rating(self, customer, score):
        """
        Registers a rating for the restaurant.

        Parameters:
        - customer (str): The name of the customer who rated.
        - score (float): The score given to the restaurant (between 1 and 5).
        """
        if 0 < score <= 5:
            rating = Rating(customer, score)
            self._ratings.append(rating)

    @property
    def average_rating(self):
        """Calculates and returns the average rating of the restaurant."""
        if not self._ratings:
            return f'-'
        total_score = sum(rating._score for rating in self._ratings)
        number_of_scores = len(self._ratings)
        average = round(total_score / number_of_scores, 1)
        return average

    def add_to_menu(self, item):
        if isinstance(item, ItemMenu): # Checks if item is an instance of ItemMenu
            self._menu.append(item)

    @property
    def display_menu(self):
        print(f'Menu of Restaurant {self._name}\n')
        for i, item in enumerate(self._menu, start=1):
            if hasattr(item, '_size') and hasattr(item, '_type'):
                message = f'{i} - {item._name.ljust(30)} | R$ {item._price:.2f} | Size: {item._size} | Type: {item._type}'
                print(message)
            elif hasattr(item, '_description'):
                message = f'{i} - {item._name.ljust(30)} | R$ {item._price:.2f} | Description: {item._description}'
                print(message)
            elif hasattr(item, '_size'):
                message = f'{i} - {item._name.ljust(30)} | R$ {item._price:.2f} | Size: {item._size}'
                print(message)
            else:
                message = f'{i} - {item._name.ljust(30)} | R$ {item._price:.2f}'
                print(message)