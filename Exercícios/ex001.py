# Crie a classe Funcionario, onde podemos cadastrar nome, setor e cargo. Crie também um método que permita o usuário se apresentar

class Funcionario:
    def __init__(self, nome = '<desconhecido>', idade = 0, cargo = '<desconhecido>'):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo

        if (self.idade <= 0):
            print('Insira uma idade válida!')
        else:
            print(f'Olá, eu sou {self.nome} tenho {self.idade} anos e sou do cargo de {self.cargo}!')

pessoa1 = Funcionario('Joaquim', 18, 'TI')