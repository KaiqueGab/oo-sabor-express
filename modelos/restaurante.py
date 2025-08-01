from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        """
        Inicializa uma instância de Restaurante.

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.
        """
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False  # Restaurante começa inativo
        self._avaliacao = [] # Lista de avaliações recebidas
        self._cardapio = []
        Restaurante.restaurantes.append(self) # Adiciona o restaurante à lista de todos

    def __str__(self):
        """Retorna uma representação em string do restaurante."""
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def listar_restaurantes(cls):
        """Exibe uma lista formatada de todos os restaurantes."""
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    def alternar_estado(self):
        """Alterna o estado de atividade do restaurante."""
        self._ativo = not self._ativo

    @property
    def ativo(self):
        """Retorna um símbolo indicando o estado de atividade do restaurante."""
        return '☑' if self._ativo else '☐'
    
    def receber_avaliacao(self, cliente, nota):
        """
        Registra uma avaliação para o restaurante.

        Parâmetros:
        - cliente (str): O nome do cliente que fez a avaliação.
        - nota (float): A nota atribuída ao restaurante (entre 1 e 5).
        """
        if 0 < nota <= 5:
            # Cria uma nova avaliação e a adiciona à lista de avaliações
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        """Calcula e retorna a média das avaliações do restaurante."""
        if not self._avaliacao:
            return f'-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media

    def adcionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio): # Verifica se o item é uma instância de ItemCardapio
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardápio do Restaurante {self._nome}\n')
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, '_tamanho') and hasattr(item, '_tipo'):    # Verifica se o item tem os atributos _tamanho e _tipo
                mensagem = f'{i} - {item._nome.ljust(30)} | R$ {item._preco:.2f} | Tamanho: {item._tamanho} | Tipo: {item._tipo}'
                print(mensagem)
            elif hasattr(item, '_descricao'):                
                mensagem = f'{i} - {item._nome.ljust(30)} | R$ {item._preco:.2f} | Descrição: {item._descricao}'
                print(mensagem)
            elif hasattr(item, '_tamanho'):    
                mensagem = f'{i} - {item._nome.ljust(30)} | R$ {item._preco:.2f} | Tamanho: {item._tamanho}'
                print(mensagem)
            else:
                mensagem = f'{i} - {item._nome.ljust(30)} | R$ {item._preco:.2f}'
                print(mensagem)