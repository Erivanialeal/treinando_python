#Simulação de um carrinho de compras
#Crie um programa que permita ao usuário adicionar produtos ao carrinho. Cada produto terá nome, preço e quantidade.
#Crie funções para adicionar produtos, remover produtos e exibir o total a pagar.
#Armazene as informações em uma estrutura adequada.

class CarrinhoDeCompras:
    def __init__(self):
        self.carrinho={} 

    def adicionar_produtos(self,nome,preco,quantidade=1):
        if nome in self.carrinho:
            self.carrinho[nome]['quantidade'] += quantidade
            print(f'{quantidade} unidade(s) de "{nome}" adicionada(s) ao carrinho.')
        else:
            self.carrinho[nome] = {'preco': preco , 'quantidade': quantidade}
            print(f'Produto "{nome}" adicionado ao carrinho.')

            
    def remover_produtos(self,nome):
        if nome in self.carrinho:
            del self.carrinho[nome]
            print(f'Produto "{nome}" removido do carrinho.')
        else:
            print(f'O produto "{nome}" não está no carrinho.')
            
        

    def total_a_pagar(self):
        total=0
        for produto in self.carrinho:
            preco= self.carrinho[produto]["preco"]
            quantidade= self.carrinho[produto]['quantidade']
            total += preco * quantidade
            print(f"Valor total a pagar: R$ {total:.2f}")


        
carrinho= CarrinhoDeCompras()
carrinho.adicionar_produtos('Arroz', 5.50, 2)
carrinho.adicionar_produtos('Feijão', 7.80, 1)
carrinho.remover_produtos('Feijão')
carrinho.total_a_pagar()