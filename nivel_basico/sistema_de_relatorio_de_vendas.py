#lembrete: estudar cada comando do codigo.

class DadosVendas:
    def __init__(self):
        self.dados = [
            {"id": 1, "nome": "Camiseta", "categoria": "Roupas", "quantidade": 5, "preco": 30.0, "data": "2024-12-10"},
            {"id": 2, "nome": "Calça", "categoria": "Roupas", "quantidade": 3, "preco": 100.0, "data": "2024-12-11"},
            {"id": 3, "nome": "Notebook", "categoria": "Eletrônicos", "quantidade": 2, "preco": 2000.0, "data": "2024-12-12"},
            {"id": 4, "nome": "Mouse", "categoria": "Eletrônicos", "quantidade": 10, "preco": 50.0, "data": "2024-12-12"},
            {"id": 5, "nome": "Tênis", "categoria": "Calçados", "quantidade": 4, "preco": 120.0, "data": "2024-12-10"}
        ]
    
    def calcular_total_produto(self):
        #sum soma 
        total = sum(item["preco"] * item["quantidade"] for item in self.dados)
        return f"O valor total dos produtos é R${total:.2f}"
    
    def produto_mais_vendido(self):
        #verifica se self.dados não está vazio
        if not self.dados:
            return "Nenhum dado encontrado."
        mais_vendido = max(self.dados, key=lambda item: item["quantidade"])
        return f"O produto mais vendido é '{mais_vendido['nome']}' com {mais_vendido['quantidade']} unidades."
    
    def calcular_total_por_categoria(self):
        total_por_categoria = {}
        for item in self.dados:
            categoria = item["categoria"]
            total_item = item["preco"] * item["quantidade"]
            if categoria in total_por_categoria:
                total_por_categoria[categoria] += total_item
            else:
                total_por_categoria[categoria] = total_item
        return total_por_categoria
    
    def gerar_relatorio(self):
        total_produto = self.calcular_total_produto()
        mais_vendido = self.produto_mais_vendido()
        total_categoria = self.calcular_total_por_categoria()
        
        relatorio = (
            "Relatório de Vendas\n"
            "----------------------\n"
            f"{total_produto}\n"
            f"{mais_vendido}\n"
            "Total por Categoria:\n"
        )
        for categoria, total in total_categoria.items():
            relatorio += f"- {categoria}: R${total:.2f}\n"
        
        return relatorio

dados_vendas = DadosVendas()
print(dados_vendas.gerar_relatorio())
