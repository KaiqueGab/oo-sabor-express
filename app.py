from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praça = Restaurante('Praça', 'Gourmet')

bebida_suco = Bebida('Suco de Laranja', 5.00, 'Médio')
bebida_suco.aplicar_desconto()

prato_salada = Prato('Salada Caesar', 15.00, 'Salada com alface, croutons e molho Caesar')
prato_salada.aplicar_desconto()

sobremesa_chocolate = Sobremesa('Brownie de Chocolate', 10.00, 'Pequeno', 'Doce', 'Brownie de chocolate com sorvete')
sobremesa_chocolate.aplicar_desconto()

restaurante_praça.adcionar_no_cardapio(bebida_suco)
restaurante_praça.adcionar_no_cardapio(prato_salada)
restaurante_praça.adcionar_no_cardapio(sobremesa_chocolate)

def main():
    restaurante_praça.exibir_cardapio
    
if __name__ == "__main__":
    main()