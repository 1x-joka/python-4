# ============= DECLARAÇÃO DE CLASSE =============
class Gafanhoto:
    def __init__(self): # Método Construtor ()
        # Atributos de Instância (características)
        self.nome = ""
        self.idade = 0

    # Métodos de Instância (o que pode fazer)
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade"

# ============= DECLARAÇÃO DE OBJETOS =============

g1 = Gafanhoto() # g1 é o objeto; o parênteses é a chamada ao método construtor na classe Gafanhoto
g1.nome = 'Maria'
g1.idade = 17
g1.aniversario()
# Se o nome depois do . não tiver parênteses é atributo, se tiver é método
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = 'Mauro'
g2.idade = 53
print(g2.mensagem())