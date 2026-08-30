# ============= POLIMORFISMO =============
# -> Python é uma das linguagens que permite Polimorfismo sem a necessidade de Herança
# -> Propriedade ou estado daquilo que se apresenta e/ou se comporta de várias formas diferentes ("um único nome mas com comportamentos diferentes")
# -> Ex.: Function Overload (como o len, a depender da situação ele da um resultado diferente)

print(len('Gustavo'))
print(len(['Curso', 'Python']))
print(len({"nome": "Maria", "idade": 22}))
print(+12)

# -> Ex2: Operator Overload (como o mais +)

print(+12)
print(5.5 + 2.2)
print('Poli' + 'Morfo')
print([1, 3, 4] + [9, 7])

# -> Polimorfismo de Inclusão/Override/Subtyping é quando um método sobrescreve um método da mãe

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome = '<desconhecido>'):
        self.nome = nome
    
    @abstractmethod
    def emitir_som(self):
        print(f'{self.nome} é {self.__class__.__name__} e está emitindo um som')

class Pato(Animal):
    def emitir_som(self):
        print(f'{self.nome} acabou de dizer QUACK! QUACK! QUACK! ')

class Cachorro(Animal):
    def emitir_som(self):
        print(f'{self.nome} acabou de dizer AU! AU! AU! ')

class Spitz(Cachorro):
    def emitir_som(self):
        print(f'{self.nome} acabou de dizer au! au! au! au! au! au! ')
    
class Pitbull(Animal):
    def emitir_som(self):
        print(f'{self.nome} acabou de dizer HULF! HULF! HULF! ')

class Gato(Animal):
    def emitir_som(self):
        print(f'{self.nome} acabou de dizer MIAU! MIAU! MIAU! ')

class Galinha(Animal):
    def emitir_som(self):
        print(f'{self.nome} acabou de dizer PÓ! PÓ! PÓ! ')

def main():
    a = Cachorro('Bandit')
    a.emitir_som()

    b = Gato('Frajola')
    b.emitir_som()

    c = Pato('Donald')
    c.emitir_som()

    d = Galinha('Pintadinha')
    d.emitir_som()

    e = Spitz('Luluzinha')
    e.emitir_som()

    f = Pitbull('Guerreiro')
    f.emitir_som()

if __name__ == '__main__':
    main()

class Mae():
    def __init__(self, nome = 'Mamãe'):
        self.nome = nome

    def fazer_pudim(self):
        print(f'{self.nome} faz PUDIM com leite condensado e calda')

    def fritar_coxinha(self):
        print(f'{self.nome} frita COXINHA no óleo de soja')

class Filha(Mae):
    def fazer_pudim(self):
        print(f'{self.nome} faz PUDIM de Leite Ninho com Nutella')
    
class Filho(Mae):
    def fritar_coxinha(self):
        print(f'{self.nome} fez COXINHA na Air Fryer')
    
p1 = Mae('Jaciara')
p2 = Filho('Matheus')
p3 = Filha('Mônica')

p1.fazer_pudim()
p1.fritar_coxinha()

p2.fazer_pudim()
p2.fritar_coxinha()

p3.fazer_pudim()
p3.fritar_coxinha()

# -> Polimorfismo de Sobrecarga/Overloading/Ad-Hoc é de finalidade
from functools import singledispatchmethod # apenas 1 parâmetro (nesse caso o valor), mas se você quiser multiplos, apenas importe a multipledispatchmethod

class Analisador():

    # Se nada for possível...
    @singledispatchmethod
    def analisar(self, valor):
        print(f'Não foi possível analisar o valor {valor}')

    @analisar.register
    def _(self, valor: int):
        print(f'{valor} é um número inteiro')

    @analisar.register
    def _(self, valor: str):
        print(f'"{valor}" é uma cadeia de caracteres')

    @analisar.register
    def _(self, valor: float):
        print(f'"{valor}" é um valor flutuante (real)')

    @analisar.register
    def _(self, valor: tuple | list | dict):
        print(f'"{valor}" é uma coleção de dados')

x = Analisador()
x.analisar('Testando')
x.analisar(3)
x.analisar(
    {
        "nome" : "Joaquim",
        "idade" : 32
    }
)
x.analisar([1, 2 ,3])
x.analisar(max([1, 2, 3])) # retorna inteiro pois ele restringe a um número (nesse caso o maior)
x.analisar(len({1, 2, 3}))

class Carteira():
    def __init__(self, valor: int | float = 0): # inteiro ou real e começa com 0
        self.__saldo = valor

    def __str__(self):
        return f"Você tem R${self.saldo:,.2f} na carteira"

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, valor):
        raise PermissionError('Você não tem autorização para alterar o saldo desse jeito')

c1 = Carteira(100)
c2 = Carteira(100)

print(c1 == c2) # eu não estou testando se o valor que ambos tem na carteira é igual, eu estou testando se os objetos são iguais, e sim, eles são da mesma classe e detém os mesmos métodos

print(c1)

    # -> Métodos para sobrescrever operadores:
        # -> equal to = .__eq__
        # -> not equal to = .__ne__
        # -> less than = .__lt__
        # -> less than or equal to = .__le__
        # -> greater than = .__gt__
        # -> greater than or equal to = .__ge_-
        # -> in-place addition = .__iadd__
        # -> in-place subtract = .__isub__

class Carteira2():
    def __init__(self, valor: int | float = 0): # inteiro ou real e começa com 0
        self.__saldo = valor

    def __str__(self):
        return f"Você tem R${self.saldo:,.2f} na carteira"

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, valor):
        raise PermissionError('Você não tem autorização para alterar o saldo desse jeito')
    
    # Sobrecarga de operadores (o igual == corresponde a o que está aqui embaixo)
    def __eq__(self, outro):
        if (self.__saldo == outro.__saldo):
            return True
        else:
            return False
        
    # o mais igual += corresponde a o que está aqui em baixo
    def __iadd__(self, valor: int | float = 0):
        self.__saldo += valor
        return self
    
c3 = Carteira2(100)
c4 = Carteira2(100)

print(c3 == c4)

c5 = Carteira2(100)
c6 = Carteira2(100)

c6 += 100 # adicionando 100 reais, totalizando 200

print(c5 == c6)

# -> Tipo de método polimórfico Duck Typing: Não importa o tipo do objeto, importa se ele executa o método

class Porta():
    def abrir(self):
        print(f'Girar a maçaneta e empurrar/puxar a porta')

class Empresa():
    def abrir(self):
        print(f'Vá ao portal do empreendedor com toda a documentação para abrir um CNPJ')

class Ovo():
    def abrir(self):
        print(f'Quebre a casca com um garfo e separe as partes sob uma frigideira')

class Pedra():
    pass

# Método Pythônico Duck Typing

def tentar_abrir(objeto):
    try:
        objeto.abrir() # tentando abrir
    except:
        print(f'Encontrei problemas ao tentar abrir um objeto tipo {objeto.__class__.__name__}') # mostra somente o nome da classe

a = Porta()
b = Empresa()
c = Ovo()
d = Pedra()

tentar_abrir(a)
tentar_abrir(b)
tentar_abrir(c)
tentar_abrir(d)

"""
    a.abrir()
    b.abrir()
    c.abrir()
    d.abrir()

    Assim dará erros específicos, pois algumas classes não tem a função abrir(), com o duck typing generaliza um pouco, não importa de tem alguma relação entre abrir uma porta, ovo, pedra, importa se o objeto tem o método abrir
"""

# -> Polimorfismo de Coerção/Ad-Hoc Coercion

# -> Polimorfismo Paramético/Templete/Generic