# Crie a seguinte estrutura de classes para calcular bônus salarial
# Funcionário (abstract): + nome, - salario, + calcular_bonus()
    # Gerente
    # Designer
    # Desenvolvedor

from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome = '<desconhecido>', salario = 0):
        self.nome = nome
        self._salario = salario

    @abstractmethod
    def calcular_bonus(self):
        pass

class Gerente(Funcionario):
    def calcular_bonus(self):
        return self._salario * 0.20

class Designer(Funcionario):
    def calcular_bonus(self):
        return self._salario * 0.20
    
class Desenvolvedor(Funcionario):
    def calcular_bonus(self):
        return self._salario * 0.15
    
gerente = Gerente('Joaquim', 10000)
designer = Designer('Maria', 5000)
desenvolvedor = Desenvolvedor('Carlos', 7000)

print(f'{gerente.nome}: R${gerente.calcular_bonus():.2f}')
print(f'{designer.nome}: R${designer.calcular_bonus():.2f}')
print(f'{desenvolvedor.nome}: R${desenvolvedor.calcular_bonus():.2f}')