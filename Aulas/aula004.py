# ============= CONTA BANCÁRIA =============

class ContaBancaria:
    """
Cria uma conta bancária e permite fazer saques e depósitos
    """

    def __init__(self, id, nt, s = 0):
        self.id = id
        self.nome_titular = nt
        self.saldo = s
        print(f'Conta {self.id} criada com sucesso. Saldo atual de R${self.saldo:.2f} no nome de {self.nome_titular}')
    
    def __str__(self):
        return f'A conta {self.id} de {self.nome_titular} tem R${self.saldo:.2f} de saldo atual'
    
    def depositar(self, valor):
        self.saldo += valor
        print(f'Depósito de R${valor:.2f} autorizado na conta {self.id}! Agora você tem R${self.saldo:.2f} de saldo atual')
    
    def sacar(self, valor):
        if (valor > self.saldo):
            print(f'Valor desejado para saque maior do que o atual da conta! Você tem R${self.saldo:.2f}')
        else:
            self.saldo -= valor
            print(f'Saque de R${valor:.2f} autorizado na conta {self.id}!')

conta1 = ContaBancaria(112, 'Gustavo', 3000)
conta1.depositar(500)
conta1.sacar(10000000)
print(conta1)