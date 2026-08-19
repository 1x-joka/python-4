# ============= MELHORANDO O CÓDIGO =============
class Gafanhoto:
    """
Essa classe cria um Gafanhoto, que é uma pessoa que tem nome e idade.
Para criar uma nova pessoa, use: variavel = Gafanhoto(nome, idade)
    """
    def __init__(self, n = '<desconhecido>', i = 0):
        self.nome = n
        self.idade = i

    def aniversario(self):
        self.idade += 1
    
    def __str__(self): # DUNDER METHOD: todo objeto tem esse método str, que é um método que mostra o endereço desse objeto na memória. A mesma função da antiga "mensagem"
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade"

print(Gafanhoto.__doc__) # Docstring

g1 = Gafanhoto('Maria', 17) # Maria é "n" e 17 é "i"
g1.aniversario()
print(g1)

g2 = Gafanhoto('Mauro', 53)
print(g2)

g3 = Gafanhoto()
print(g3)

print('-' * 15)
print(g1.__dict__) # é um atributo, não tem parênteses
print(g1.__getstate__()) # é um método, veja o parênteses
print(g1.__class__) # Dunder Method (g1 é um objeto da classe Gafanhoto)
print(g1.__doc__) # Dunder Attribute