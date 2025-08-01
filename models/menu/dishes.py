from models.menu.item_menu import ItemMenu

class Dishes(ItemMenu): # Passing ItemMenu as superclass means Dishes inherits its attributes and methods
    def __init__(self, name, price, description):
        super().__init__(name, price) # Calls the constructor of the superclass ItemMenu
        self._description = description 

    def __str__(self):
        return f"Dish: {self._name}, Price: R${self._price:.2f}, Description: {self._description}"
    
    def apply_discount(self):
        self._price -= (self._price * 0.05)