# ============= ENCAPSULAMENTO =============
# -> Visa manter a integridade do sistema, protegendo o estado interno do objeto contra interferência externa não regulamentada 
    # Ex.: O que fazemos para proteger os circuitos e componentes externos e um controle remoto? Envolvemos ele em uma "cápsula" que deixa exposto apenas o que é acessível
    # Ex.: Qual é o objetivo de usar uma cápsula gelatinosa nos remédios? Isola a dose exata dos compostos; Impede a ação de fatores externos (umidade, luz, etc.); Protege o paciente do gosto amargo e da toxicidade direta
# -> Principais Vantagens
    # -> Segurança e Controle
    # -> Facilidade de Manutenção
    # -> Flexibilidade e Reutilização
    # -> Redução de efeitos colaterais

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
        return f'Estado atual da conta: {self.__dict__}'
    
    def depositar(self, valor):
        self.saldo += valor
        print(f'Depósito de R${valor:.2f} autorizado na conta {self.id}! Agora você tem R${self.saldo:.2f} de saldo atual')
    
    def sacar(self, valor):
        if (valor > self.saldo):
            print(f'Valor desejado para saque maior do que o atual da conta! Você tem R${self.saldo:.2f}')
        else:
            self.saldo -= valor
            print(f'Saque de R${valor:.2f} autorizado na conta {self.id}!')

def main():
    c1 = ContaBancaria(111, 'Maria', 5000)
    c1.depositar(-500) # Falha de Segurança
    c1.sacar(-100) # Falha de Segurança
    c1.saldo = 0 # Falha de Segurança, tirando todo o dinheiro dela
    print(c1)

if (__name__ == '__main__'):
    main()

# -> Para realizar essa proteção, precisamos entender:
    # -> Visibilidade de Atributos
    # -> Acesso aos dados protegidos
    
# -> Visibilidade de Atributos
    # -> Existem três tipos de visibilidade para atributos em linguagens POO:
        # -> public + (disponível em todo o escopo: classe mãe, classe filha e todo o código restante)
        # -> protected # (disponível para a classe atual e as subclasses, não permitindo alteração no código restante como o principal por exemplo: o main)
        # -> private - (somente naquela classe específica, as classes filhas e o restante não)
    # -> Consenting Adults: Liberdade com Responsabilidade, o Python não priva totalmente um dado, apenas sugere para o desenvolvedor que ele não mexa, mas ele pode.
    # -> Sempre que tiver um atributo público, no Python, não coloca nada
    # -> Sempre que tiver um atributo protegido, coloca um underline na frente
    # -> Sempre que tiver um atributo protegido, coloca um duplo underline na frente (Name Mangling)

class ContaBancaria:
    """
Cria uma conta bancária e permite fazer saques e depósitos
    """

    def __init__(self, id, nt, s = 0):
        self.id = id # público
        self._nome_titular = nt # protegido
        self.__saldo = s # privado
        print(f'Conta {self.id} criada com sucesso. Saldo atual de R${self.__saldo:.2f} no nome de {self._nome_titular}')
    
    def __str__(self):
        return f'Estado atual da conta: {self.__dict__}'
    
    def depositar(self, valor):
        valor = abs(valor) # tornando o negativo positivo, como um |n|
        self.__saldo += valor
        print(f'Depósito de R${valor:.2f} autorizado na conta {self.id}! Agora você tem R${self.__saldo:.2f} de saldo atual')
    
    def sacar(self, valor):
        valor = abs(valor)
        if (valor > self.__saldo):
            print(f'Valor desejado para saque maior do que o atual da conta! Você tem R${self.__saldo:.2f}')
        else:
            self.__saldo -= valor
            print(f'Saque de R${valor:.2f} autorizado na conta {self.id}!')

def main2():
    c2 = ContaBancaria(111, 'Maria', 5000)
    c2.nt = 'Pedro' # não permite alterar o Maria, mas cria um novo atributo
    c2._nome_titular = 'Pedro' # agora sim alterou
    c2.depositar(-500)
    c2.sacar(-100)

    c2.__saldo = 0 # ainda não alterou, pois é privado
    c2.saldo = 0 # ainda não alterou
    c2._ContaBancaria__saldo = 0 # agora sim alterou, mas olha o quanto eu tive que escrever para mudar, você tem que querer muito zerar a conta, não tem como ser sem querer
    print(c2)

if (__name__ == '__main__'):
    main2()

# -> Métodos Acessores (maneiras de permitir o acesso aos dados encapsulados)
    # -> Getters
    # -> Setters
    # -> @property

from rich import inspect, print

class Avaliacao():
    def __init__(self, nome = '<desconhecido>', disciplina = '<desconhecido>', nota = 0):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota

    def get_nota(self): # método getter
        return self._nota

    def set_nota(self, valor): # método setter
        if (0 <= valor <= 10):
            self._nota = valor
        else:
            print('Nota inválida')

def main3():
    av1 = Avaliacao('Pedro', 'Matemática', 9.5)
    av1.set_nota(-5) # não muda pois o getter impede isso
    print(f'{av1.nome} tirou {av1.get_nota()} em {av1.disciplina}')
    inspect(av1, private = True)

if __name__ == '__main__':
    main3()

# -> @property: automaticamente faz a validação sem precisar de uma função escrita no código. Exemplo de property: @nota.getter

class Avaliacao():
    def __init__(self, nome = '<desconhecido>', disciplina = '<desconhecido>', nota = 0):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota

    # Criando Atributo Validável
    @property
    def nota(self): # criando um atributo novo, um caminho para validar a nota; getter
        return self._nota
    
    @nota.setter
    def nota(self, valor): # setter
        if (0 <= valor <= 10):
            self._nota = valor
        else:
            print('Nota inválida')

    @nota.deleter
    def nota(self):
        print('Não pode deletar uma nota!')

def main4():
    av2 = Avaliacao('Pedro', 'Matemática', 9.5)
    av2.nota = 3.5
    av2.nota = -7.2
    print(f'{av2.nome} tirou {av2.nota} em {av2.disciplina}') # av2.nota está chamando o novo atributo (def nota) não o original
    inspect(av2, private = True)

if __name__ == '__main__':
    main4()