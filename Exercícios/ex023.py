# Implemente a seguinte estrutura com agregação, incluindo sobrecarga do operador + para adicionar produtos ao carrinho de compras
# Carrinho: + produtos [0...n], + @total
    # Produto: + nome, + preco

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Carrinho:
    def __init__(self):
        self.produtos = []

    @property
    def total(self):
        return sum(produto.preco for produto in self.produtos)

    def __add__(self, produto):
        self.produtos.append(produto)
        return self

produto1 = Produto('Teclado', 150.00)
produto2 = Produto('Mouse', 80.00)
produto3 = Produto('Monitor', 900.00)

carrinho = Carrinho()

carrinho + produto1
carrinho + produto2
carrinho + produto3

print(f'Produtos no carrinho:')

for produto in carrinho.produtos:
    print(f'- {produto.nome}: R${produto.preco:.2f}')

print(f'\nTotal: R${carrinho.total:.2f}')