# Crie classes capazes de calcular fretes de veículos diferentes:
# Transporte (abstract) ancestral: distancia, frete, calc_frete() abstract
# Moto: fator = 0.50, calc_frete() livre
# Caminhão: fator = 1.20, calc_frete() mínimo de 50km
# Drone: fator = 9.50, calc_frete() máximo de 10km
from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, distancia = 0, frete = 0):
        self.distancia = distancia
        self.frete = frete
    
    @abstractmethod
    def calc_frete(self):
        pass

class Moto(Transporte):
    def __init__(self, distancia=0, frete=0):
        super().__init__(distancia, frete)
        self.fator = 0.50
    
    def calc_frete(self):
        self.frete = self.distancia * self.fator
        print(f'O frete para transporte de moto é R${self.frete:.2f}')

class Caminhão(Transporte):
    def __init__(self, distancia=0, frete=0):
        super().__init__(distancia, frete)
        self.fator = 1.20
    
    def calc_frete(self):

        if (self.distancia >= 50):
            self.frete = self.distancia * self.fator
            print(f'O frete para transporte de caminhão é R${self.frete:.2f}')
        else:
            print('Insira uma distância maior ou igual a 50km')

class Drone(Transporte):
    def __init__(self, distancia=0, frete=0):
        super().__init__(distancia, frete)
        self.fator = 9.50
    
    def calc_frete(self):
        
        if (self.distancia < 10):
            self.frete = self.distancia * self.fator
            print(f'O frete para transporte de drone é R${self.frete:.2f}')
        else:
            print('Insira uma distância menor ou igual que 10km')

moto = Moto(20)
moto.calc_frete()

caminhao = Caminhão(50)
caminhao.calc_frete()

drone = Drone(10)
drone.calc_frete()