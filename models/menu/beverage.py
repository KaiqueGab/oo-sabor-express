from models.menu.item_menu import ItemMenu

class Beverage(ItemMenu):
    def __init__(self, name, price, size):
        super().__init__(name, price)  # Calls the constructor of the superclass ItemMenu
        self._size = size  

    def __str__(self):
        return f"Beverage: {self._name}, Price: R${self._price:.2f}, Size: {self._size}"
    
    def apply_discount(self):
        self._price -= (self._price * 0.08)