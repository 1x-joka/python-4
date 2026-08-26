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

# -> Polimorfismo de Coerção/Ad-Hoc Coercion

# -> Polimorfismo Paramético/Templete/Generic

# -> Tipo de método polimórfico: Duck Typing