# Crie classes para validadores de dados, com os exemplos a seguir:
# Validador (abstract): + validar()
    # Usuario (de 5 a 20 caracteres, letras minúsculas, numeros e símbolo de sublinhado)
        # Email (deve conter uma única @, usuário pode conter letras, números e alguns símbolos, os domínios contém pontos e o TLD encerra com ponto e pelo menos 2 letras)
        # Senha (pelo menos 8 caracteres, pelo menos uma maiúscula e pelo menos um símbolo)

from abc import ABC, abstractmethod
import re

class Validador(ABC):

    @abstractmethod
    def validar(self, valor):
        pass

class Usuario(Validador):

    def validar(self, valor):
        """
        Usuário:
        - de 5 a 20 caracteres
        - letras minúsculas
        - números
        - símbolo '_'
        """

        return bool(re.fullmatch(r'[a-z0-9_]{5,20}', valor))

class Email(Validador):

    def validar(self, valor):
        """
        E-mail:
        - deve possuir uma única '@'
        - usuário pode conter letras, números e alguns símbolos
        - domínio deve possuir pontos
        - TLD deve terminar com pelo menos 2 letras
        """

        padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*\.[a-zA-Z]{2,}$'

        return bool(re.fullmatch(padrao, valor))

class Senha(Validador):

    def validar(self, valor):
        """
        Senha:
        - pelo menos 8 caracteres
        - pelo menos uma letra maiúscula
        - pelo menos um símbolo
        """

        if len(valor) < 8:
            return False

        if not re.search(r'[A-Z]', valor):
            return False

        if not re.search(r'[^a-zA-Z0-9]', valor):
            return False

        return True

usuario = Usuario()
email = Email()
senha = Senha()

print('USUÁRIO')
print(usuario.validar('joaquim_123'))  # True
print(usuario.validar('Joaquim123'))   # False
print(usuario.validar('joq'))          # False

print('\nEMAIL')
print(email.validar('joaquim@gmail.com')) # True
print(email.validar('joaquim@gmail')) # False
print(email.validar('joaquim@@gmail.com')) # False

print('\nSENHA')
print(senha.validar('Joaquim@123')) # True
print(senha.validar('joaquim123')) # False
print(senha.validar('JOAQ@')) # False