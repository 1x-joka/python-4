# Crie a classe Produto, onde podemos cadastrar nome e preço. Crie também um método que mostre uma etiqueta de preço do produto

from rich.panel import Panel
from rich import print

class Produto:
    def __init__(self, nome = '<desconhecido>', preco = 0):
        self.nome = nome

        if (preco < 0):
            print('[red]Insira um valor válido![/]')
            self.preco = 0
        else:
            self.preco = preco
    
    def etiqueta(self):
        texto = f'O produto é {self.nome} e o preço é de R${self.preco:.2f}'
        print(Panel(texto, title = 'Etiqueta do Produto', border_style = 'green', expand = False)) # expand = False se adapta ao tamanho do texto dentro da caixa

produto1 = Produto('Iphone 17 Pro Max', 10000)
produto1.etiqueta()