# Crie um simulador que gerencie o pagamento em diferentes tipos
# Pagamento (abstract): # valor, + @fvalor, + pagar()
    # Boleto
    # PIX
    # Crédito

from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, valor = 0):
        self._valor = valor
    
    @property
    def fvalor(self):
        return f'R${self._valor:,.2f}'
    
    @abstractmethod
    def pagar(self):
        pass

class PIX(Pagamento):
    def pagar(self):
        print(f'Pagamento de {self._valor} realizado via PIX')
    
class Boleto(Pagamento):
    def pagar(self):
        print(f'Pagamento de {self._valor} realizado via Boleto')

class Credito(Pagamento):
    def pagar(self):
        print(f'Pagamento de {self._valor} realizado via Crédito')

boleto = Boleto(150.50)
pix = PIX(75.90)
credito = Credito(320.00)

print(f'Valor do boleto: {boleto.fvalor}')
boleto.pagar()

print()

print(f'Valor do PIX: {pix.fvalor}')
pix.pagar()

print()

print(f'Valor do crédito: {credito.fvalor}')
credito.pagar()