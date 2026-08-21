from pessoa import Pessoa

class Aluno(Pessoa): # ao criar um aluno, ele irá herdar as características da superclasse "Pessoa", se tornando uma subclasse
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade) # indicando para ir na superclasse e executar o init dela
        self.curso = curso
        self.turma = turma
    
    def fazerMatricula(self):
        print(f'{self.nome} acabou de fazer matrícula!')