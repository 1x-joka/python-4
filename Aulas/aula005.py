# ============= RICH: CORES, EMOJIS, TABELAS E DEBUG MAIS BONITOS =============

from rich import print # substitui o print anteriormente (comum) pelo do rich (com funcionalidades novas)
from rich.panel import Panel # 
print('Hello, [red]World[/]! :earth_americas:')
print('Olá, [bold blue on purple]Pequeno Gafanhoto[/] :vulcan_salute:') # negrito com a cor azul e fundo roxo

caixa = Panel('Esse aqui é um painel de exemplo', title = 'Mensagem', style = 'purple', width = 30) # instanciando um objeto 'caixa' da classe 'Panel'
print(caixa)

from rich.table import Table
tabela = Table(title = 'Tabela de Preços')

tabela.add_column('Nome', justify = 'center', style = 'blue') # os nomes estarão com cor azul
tabela.add_column('Preço', justify = 'center', style = 'purple')

tabela.add_row('Lápis', 'R$1,50')
tabela.add_row('Borracha', '[green]R$5,00[/]') # o verde irá sobrescrever a roxa

print(tabela)

from rich import inspect
inspect(int)
inspect(float, all = True) # muito mais completo que o de cima

# Melhorando o sistema de conta bancária

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
inspect(conta1)

# Deixando a mostra do erro mais bonito

from rich.traceback import install
install() # a partir daqui, todos os erros que acontecerem no sistemas serão monitorados pelo rich e exibido mais bonito e detalhado

def divisao(x, y):
    return x / y

divisao(25, 0)