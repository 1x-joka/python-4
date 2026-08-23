# Implemente o seguinte diagrama de classes:
# Polígono (abstract) ancestral: qtd_lados, perimetro() abstract e area() abstract
# Quadrado: lado, perimetro() e area()
# Círculo: raio, perimetro() e area()
from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self, qtd_lados = 0):
        self.qtd_lados = qtd_lados
    
    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass
    
class Quadrado(Poligono):
    def __init__(self, lado = 0):
        super().__init__(4) # um quadrado tem 4 lados
        self.lado = lado
    
    def perimetro(self):
        p = self.lado * 4
        print(f'O perímetro do quadrado de lado {self.lado} é {p}m')
    
    def area(self):
        a = self.lado ** 2
        print(f'A área do quadrado de lado {self.lado} é {a}m²')

class Circulo(Poligono):
    def __init__(self, raio = 0):
        super().__init__(0) # um círculo tem 0 lados
        self.raio = raio
    
    def perimetro(self):
        p = 2 * 3.13 * self.raio
        print(f'O perímetro do círculo de raio {self.raio} é {p}m')
    
    def area(self):
        a = 3.14 * (self.raio ** 2)
        print(f'A área do círculo de raio {self.raio} é {a}m²')

quadrado = Quadrado(5)
quadrado.perimetro()
quadrado.area()

circulo = Circulo(5)
circulo.perimetro()
circulo.area()