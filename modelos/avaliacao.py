import os 
os.system('cls')

class Avaliacao:

    def __init__(self, cliente, nota):
        self._cliente = cliente
        self._nota = nota

    def __str__(self):
        return f'Avaliação de {self._cliente}: Nota {self._nota}'