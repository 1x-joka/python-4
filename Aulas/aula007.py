# ============= ABSTRAÇÃO =============
# -> Pratica de ignorar o irrelevante e focar estritamente no essencial
# -> Principais Vantagens
    # -> Maior legibilidade
    # -> Padronização
    # -> Simplificação
    # -> Segurança
# -> Existe a abstração de dados, que acontece quando ignoramos informações desnecessárias para o escopo do projeto (peso é comum de uma pessoa, mas para um sistema de escola por exemplo não é preciso). Existe a abstração de processos, quando não precisamos saber como um método faz seu trabalho, apenas sabe que ela existe pela interface (não saber como uma biblioteca no python funciona, por exemplo.)
# -> Classe Abstrata é aquela classe que não serve para gerar objetos, e sim para funcionar como uma base para todas as subclasses se tornarem um objeto
# -> Classe Concreta é aquela que, de fato, irão se tornar objetos
# -> Método Abstrato é aquele método que está na classe mãe abstrata e não tem linha de programação para ele, mas indica que os filhos da classe mãe terão que ter aquele método, aquela funcionalidade
# -> Método Concreto é aquele método que é desenvolvido na classe mãe, com linhas de código mesmo
# -> ABC (Abstract Base Classes) é uma biblioteca que nos permite indicar que a classe é uma Abstração
# -> DRY (Don't Repeat Yourself) é 

from rich import print, inspect
from abc import ABC, abstractmethod

class Pessoa(ABC): # Agora é uma classe abstrata
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1

    @abstractmethod # abaixo disso terá um método abstratp
    def estudar(self): # todas as filhas (Aluno, Professor e Funcionário) terão que ter essa funcionalidade obrigatoriamente da maneira que quiser
        ...
    
class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma
    
    def fazerMatricula(self):
        print(f'{self.nome} acabou de fazer matrícula!')

    def estudar(self):
        print(f'{self.nome} está estudando {self.curso} na turma {self.turma}')

class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel
    
    def darAula(self):
        print(f'Prof. {self.nome} começou a dar aula!')
    
    def estudar(self):
        print(f'{self.nome} é especialista em {self.especialidade} no {self.nivel}')

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor
    
    def baterPonto(self):
        print(f'{self.nome} acabou de bater ponto!')

    def estudar(self):
        print(f'{self.nome} se especializa para a área de {self.setor}')

aluno1 = Aluno('José', 17, 'Informática', 'T01')
aluno1.fazer_aniversario()
aluno1.fazerMatricula()
aluno1.estudar()
inspect(aluno1, methods = True)

professor1 = Professor('Samuel', 37, 'Biologia', 'Mestrado')
professor1.darAula()
professor1.estudar()
inspect(professor1, methods = True)

funcionario1 = Funcionario('Cláudia', 27, 'Secretária Escolar', 'Secretaria')
funcionario1.fazer_aniversario()
funcionario1.baterPonto()
funcionario1.estudar()
inspect(funcionario1, methods = True)