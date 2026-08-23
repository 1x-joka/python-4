# Simule uma cafeteria orientada a objetos:
# BebidaQuente (abstract) ancestral: preparar(), ferver_agua(), misturar() abstract e servir() abstract
# Café: misturar(), servir()
# Chá: misturar(), servir()
# Leite: misturar(), servir()
from abc import ABC, abstractmethod

class BebidaQuente(ABC):
    def preparar(self):
        print('Preparando..')
    
    def ferver_agua(self):
        print('Fervendo..')
    
    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass

class Cafe(BebidaQuente):
    
    def misturar(self):
        print('Misturando..')

    def servir(self):
        print('Servindo..')

class Cha(BebidaQuente):

    def misturar(self):
        print('Misturando..')

    def servir(self):
        print('Servindo..')

class Leite(BebidaQuente):

    def misturar(self):
        print('Misturando..')

    def servir(self):
        print('Servindo..')

cafe = Cafe()
cafe.preparar()
cafe.ferver_agua()
cafe.misturar()
cafe.servir()