# Crie a estrutua capaz de calcular salários de funcionários diferentes:
# Funcionário (abstract) ancestral: nome, sal_bruto, salario, sal_min = 1612, inss = 7.50
# Honorista: valor_hora, horas_trab, calc_sal()
# Mensalista: calc_sal()
from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome = '<desconhecido>', sal_bruto = 0, salario = 0):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.salario = salario
        self.sal_min = 1612
        self.inss = 7.50

class Honorista(Funcionario):
    def __init__(self, nome='<desconhecido>', sal_bruto = 0, salario = 0, valor_hora = 0, horas_trab = 0):
        super().__init__(nome, sal_bruto, salario)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab
    
    def calc_sal(self):
        self.sal_bruto = self.valor_hora * self.horas_trab
        self.salario = self.sal_bruto - (self.sal_bruto * self.inss / 100)
        print(f'O salário do(a) honorista {self.nome} é {self.salario}')

class Mensalista(Funcionario):
    def calc_sal(self):
        self.salario = self.sal_bruto - (self.sal_bruto * self.inss / 100)
        print(f'O salário do(a) mensalista {self.nome} é {self.salario}')

honorista = Honorista(nome = 'Joaquim', valor_hora = 20, horas_trab = 160)

mensalista = Mensalista(nome = 'Diana', sal_bruto = 320)

honorista.calc_sal()
mensalista.calc_sal()