# ============= HERANÇA =============
# -> relacionamento, do tipo "é 1", entre itens gerais (ancestrais) e tipos mais específicos (descentendes) desses itens, que heram atributos e métodos dos níveis superiores
# -> Principais Vantagens
    # Reutilização de código
    # Organização Hierárquica
    # Facilita manutenção
    # Extensibilidade
    # Suporte a polimorfismo

# -> A classe acima da herança é chamada de "superclasse" (classe base, ancestral, classe mãe). E a abaixo é "subclasse" (classe derivada, descendente, classe filha)
# Ex.: se em um sistema de escola, o aluno, professor e funcionário tem classes em métodos em comuns (como fazer aniversario) e classes (como nome e idade), como um banco de dados, eu não preciso repetir esses métodos e classes em cada objeto (pessoa) e sim criar um outro objeto somente com esses atributos, ou seja, os três objetos irão herdar algumas características desse quarto

from rich import print, inspect

class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1
    
class Aluno(Pessoa): # ao criar um aluno, ele irá herdar as características da superclasse "Pessoa", se tornando uma subclasse
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade) # indicando para ir na superclasse e executar o init dela
        self.curso = curso
        self.turma = turma
    
    def fazerMatricula(self):
        print(f'{self.nome} acabou de fazer matrícula!')

class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel
    
    def darAula(self):
        print(f'Prof. {self.nome} começou a dar aula!')

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor
    
    def baterPonto(self):
        print(f'{self.nome} acabou de bater ponto!')

aluno1 = Aluno('José', 17, 'Informática', 'T01')
aluno1.fazer_aniversario()
aluno1.fazerMatricula()
inspect(aluno1, methods = True)

professor1 = Professor('Samuel', 37, 'Biologia', 'Mestrado')
professor1.darAula()
inspect(professor1, methods = True)

funcionario1 = Funcionario('Cláudia', 27, 'Secretária Escolar', 'Secretaria')
funcionario1.fazer_aniversario()
funcionario1.baterPonto()
inspect(funcionario1, methods = True)