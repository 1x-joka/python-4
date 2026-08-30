# Implemente um sistema de mensagens padronizadas usando orientação a objetos
# Mensagem: # mensagem, # tipo, # icone, + mostrar()
    # Erro
    # Aviso

from abc import ABC, abstractmethod

class Mensagem(ABC):

    def __init__(self, mensagem):
        self._mensagem = mensagem
        self._tipo = ''
        self._icone = ''

    @abstractmethod
    def mostrar(self):
        pass

class Erro(Mensagem):

    def __init__(self, mensagem):
        super().__init__(mensagem)
        self._tipo = 'ERRO'
        self._icone = '❌'

    def mostrar(self):
        print(f'{self._icone} [{self._tipo}] {self._mensagem}')

class Aviso(Mensagem):

    def __init__(self, mensagem):
        super().__init__(mensagem)
        self._tipo = 'AVISO'
        self._icone = '⚠️'

    def mostrar(self):
        print(f'{self._icone} [{self._tipo}] {self._mensagem}')


erro = Erro('Não foi possível realizar a operação.')
aviso = Aviso('Sua senha irá expirar em 5 dias.')

erro.mostrar()
aviso.mostrar()