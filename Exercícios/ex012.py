# Simule o sistema de batalha entre personagens de um RPG
# Personagem (abstract) ancestral: nome, vida, golpes, atacar(alvo, forca), receber_dano(dano), curar() abstract
# Guerreiro: curar()
# Mago: curar()
from abc import ABC, abstractmethod

class Personagem(ABC):
    def __init__(self, nome = '<desconhecido>', vida = 0, golpes = 0):
        self.nome = nome
        self.vida = vida
        self.golpes = golpes

    def receber_dano(self, dano):
        self.vida -= dano # tirando vida de fato

        if (self.vida <= 0):
            self.vida = 0
            print(f'{self.nome} morreu')
        else:
            print(f'{self.nome} recebeu dano de {dano}hp')
    
    def atacar(self, alvo, forca):
        print(f'{self.nome} atacando {alvo.nome}')
        alvo.receber_dano(forca)

    @abstractmethod
    def curar(self):
        pass

class Guerreiro(Personagem):
    def curar(self):
        self.vida += 20
        print(f'{self.nome} curou 20 pontos e agora está com {self.vida}hp')

class Mago(Personagem):
    def curar(self):
        self.vida += 30
        print(f'{self.nome} se curou 30 pontos e agora está com {self.vida}hp')

guerreiro1 = Guerreiro('Joaquim', 100, 10)
mago = Mago('Gandalf', 80, 15)

guerreiro1.atacar(mago, 20)
mago.atacar(guerreiro1, 15)

guerreiro1.curar()
mago.curar()