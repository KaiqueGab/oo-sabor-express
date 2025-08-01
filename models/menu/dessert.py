from models.menu.item_menu import ItemMenu

class Dessert(ItemMenu):
    def __init__(self, name, price, size, type_, description):
        super().__init__(name, price)
        self._size = size
        self._type = type_
        self._description = description

    def __str__(self):
        return f"Dessert: {self._name}, Price: R${self._price:.2f}, Size: {self._size}, Type: {self._type}, Description: {self._description}"
    
    def apply_discount(self):
        self._price -= (self._price * 0.10)