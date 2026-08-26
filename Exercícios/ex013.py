# Implemente um termostato orientado a objetos
# Mínimo: 16°C
# Incremento: 0.5°C
# Máximo: 30°C
# __temperatura, @temperatura, @ftemperatura

class Termostato():
    def __init__(self, temperatura = 0):
        self.__temperatura = temperatura
    
    @property
    def temperatura(self):
        return self.__temperatura
    
    @temperatura.setter
    def temperatura(self, temperatura):
        if (temperatura < 16):
            self.__temperatura = 16
        elif (temperatura > 30):
            self.__temperatura = 30
        else:
            self.__temperatura = temperatura

    @property
    def ftemperatura(self):
        return self.__temperatura + 0.5
    
    @ftemperatura.setter
    def ftemperatura(self, temperatura):
        if (temperatura < 16):
            self.__temperatura = 16
        elif (temperatura > 30):
            self.__temperatura = 30
        else:
            self.__temperatura = temperatura