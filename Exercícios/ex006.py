# Crie a classe Caneta, que simule o funcionamento de uma caneta colorida, podendo escrever frases na cor relativa
from rich import print

class Caneta():
    def __init__(self, frase = '<desconhecido>', vermelho = False, azul = False, verde = False, amarelo = False, verificacao = False):
        self.frase = frase
        self.vermelho = vermelho
        self.azul = azul
        self.verde = verde
        self.amarelo = amarelo
        self.verificacao = verificacao

    def escreverVermelho(self):
        if (self.vermelho):
            print(f'Em vermelho: \n[red]{self.frase}[/]')
    
    def escreverAzul(self):
        if (self.azul):
            print(f'Em azul: \n[blue]{self.frase}[/]')

    def escreverVerde(self):
        if (self.verde):
            print(f'Em verde: \n[green]{self.frase}[/]')

    def escreverAmarelo(self):
        if (self.amarelo):
            print(f'Em amarelo: \n[yellow]{self.frase}[/]')

    def abrirCaneta(self):
        if self.verificacao:
            print('A caneta já está aberta!')
        else:
            self.verificacao = True
            print('Abrindo a caneta..')

    def fecharCaneta(self):
        if not (self.verificacao):
            print('A caneta já está fechada!')
        else:
            self.verificacao = False
            print('Fechando a caneta..')


escrita = Caneta('Olá Joaquim!', True, True, True, True)
escrita.abrirCaneta()
escrita.abrirCaneta()
escrita.fecharCaneta()
escrita.abrirCaneta()
print('-' * 15)
escrita.escreverVermelho()
escrita.escreverAzul()
escrita.escreverVerde()
escrita.escreverAmarelo()
print('-' * 15)
escrita.fecharCaneta()
escrita.fecharCaneta()