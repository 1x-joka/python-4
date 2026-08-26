# Aprimore o exercício da ContaBancaria, aplicando conceitos de encapsulamento
# ContaBancaria: _id, _titular, __saldo, __hash, @nome, validar_senha(chave), pede_senha(), sacar(valor, chave), depositar(valor)
import hashlib

class ContaBancaria:
    """
Representa uma conta bancária.
O saldo e a senha são protegidos por encapsulamento.
    """

    def __init__(self, id, titular, senha, saldo = 0):
        self._id = id
        self._titular = titular
        self.__saldo = saldo
        self.__hash = hashlib.sha256(senha.encode()).hexdigest()

    @property
    def nome(self):
        return self._titular

    def validar_senha(self, chave): # gera o hash da senha informada e compara com o hash armazenado
        hash_chave = hashlib.sha256(chave.encode()).hexdigest()
        return hash_chave == self.__hash

    def pede_senha(self):
        return input('Digite sua senha: ')

    def sacar(self, valor, chave):
        if not self.validar_senha(chave):
            print('Senha incorreta.')
            return

        if valor <= 0:
            print('O valor do saque deve ser maior que zero.')
            return

        if valor > self.__saldo:
            print('Saldo insuficiente.')
            return

        self.__saldo -= valor
        print(f'Saque de R${valor:.2f} realizado com sucesso.')
        print(f'Saldo atual: R${self.__saldo:.2f}')

    def depositar(self, valor):
        if valor <= 0:
            print('O valor do depósito deve ser maior que zero.')
            return

        self.__saldo += valor
        print(f'Depósito de R${valor:.2f} realizado com sucesso.')
        print(f'Saldo atual: R${self.__saldo:.2f}')


# ============= TESTES =============

conta = ContaBancaria(1, 'Joaquim', '1234', 1000)
print(f'Titular: {conta.nome}')
conta.depositar(500)
conta.sacar(200, '1234')
conta.sacar(100, '9999')
conta.sacar(2000, '1234')