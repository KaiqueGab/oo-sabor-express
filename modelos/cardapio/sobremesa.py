from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, tamanho, tipo, descricao):
        super().__init__(nome, preco)
        self._tamanho = tamanho
        self._tipo = tipo
        self._descricao = descricao

    def __str__(self):
        return f"Sobremesa: {self._nome}, Preço: R${self._preco:.2f}, Tamanho: {self._tamanho}, Tipo: {self._tipo}, Descrição: {self._descricao}"
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.10)