from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio): #Passar a classe ItemCardapio como superclasse, quer dizer que a classe Prato herda os atributos e métodos de ItemCardapio
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco) #Chama o construtor da superclasse ItemCardapio
        self._descricao = descricao 

    def __str__(self):
        return f"Prato: {self._nome}, Preço: R${self._preco:.2f}, Descrição: {self._descricao}"
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)