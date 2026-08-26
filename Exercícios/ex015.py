# Crie uma classe que gerencie a hash SHA256 de uma senha
# Credencial: @senha, __hash, validar(chave)
import hashlib as hash

class VerificadorSenha():
    def __init__(self, senha = ''):
        self.senha = senha

    @property
    def senha(self):
        return '******' # "criptografando" ela (deixando irreconhecível)
    
    @senha.setter
    def senha(self, senha):
        self.__hash = hash.sha256(senha.encode()).hexdigest() # hasheando a senha e guardando nessa variável
    
    def validar(self, chave):
        hash_chave = hash.sha256(chave.encode()).hexdigest()

        if (hash_chave == self.__hash):
            print('Senha válida')
        else:
            print('Senha inválida')

teste = VerificadorSenha('1234')
print(teste.senha)

teste.validar('1234') # validando de fato
teste.validar('0000')