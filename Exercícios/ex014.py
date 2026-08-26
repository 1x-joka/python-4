# Simule um diário secreto orientado a objetos
# Diário: __segredos[], __senha, escrever(msg), ler(senha)

class Diario():
    def __init__(self, senha = ''):
        self.__segredos = []
        self.__senha = senha
    
    def escrever(self, msg):
        self.__segredos.append(msg)
        print('Segredo registrado!')

    def ler(self, senha):
        if (senha == self.__senha):
            print('Segredos:')
            for segredo in self.__segredos:
                print(segredo)
        else:
            print('Senha incorreta!')

diario = Diario('1234') # essa é a senha
diario.escrever('Hoje estudei Python')

diario.ler('1234')
diario.ler('0000')