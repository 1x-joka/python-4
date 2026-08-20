# Crie a classe Churrasco, onde seja possível informar quantas pessoas vão participar e mostre quanto de carve deve ser comprado, o custo total do churrasco e o preço por pessoa

class Churrasco():

    """
Assumimos que cada pessoa consuma 2kg de carne e o preço por pessoa é de R$10,00
    """

    def __init__(self, qtd_pessoas):
        self.qtd_pessoas = qtd_pessoas

        self.calculoCarne()
        self.calculoTotal()
        self.calculoPrecoPessoa()
        self.calculoTotal2()

    def calculoCarne(self):
        self.qtd_carne = self.qtd_pessoas * 2

    def calculoTotal(self):
        self.custo = self.qtd_pessoas * 10

    def calculoPrecoPessoa(self):
        self.preco_pessoa = self.custo / self.qtd_pessoas
    
    def calculoTotal2(self):
        self.custo2 = self.custo + (self.preco_pessoa * self.qtd_pessoas)
    
    def mensagem(self):
        return f'Como vão {self.qtd_pessoas} pessoas, será preciso {self.qtd_carne}kg, o custo total será R${self.custo:.2f} (sem o preço por pessoa) e o preço por pessoa é de R${self.preco_pessoa:.2f}, totalizando R${self.custo2:.2f}'

meu_churrasco = Churrasco(5)
print(meu_churrasco.mensagem())