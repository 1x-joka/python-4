# Implemente o seguinte estrutura de diagrama de classes
# Pessoa: _nome, _nascimento, @nascimento, @idade
# Aluno (filho de Pessoa): cursos_oficiais, _curso, @curso, add_curso(curso)
from datetime import date

class Pessoa():
    def __init__(self, nome = '<desconhecido>', nascimento = 0):
        self._nome = nome
        self._nascimento = nascimento
    
    @property
    def nascimento(self):
        return self._nascimento
    
    @property
    def idade(self):
        hoje = date.today()
        idade = hoje.year - self._nascimento.year

        if (hoje.month, hoje.day) < (self._nascimento.month, self._nascimento.day):
            idade -= 1
        
        return idade

class Aluno(Pessoa):
    def __init__(self, nome = '<desconhecido>', nascimento = 0, curso = ''):
        super().__init__(nome, nascimento)
        self.cursos_oficiais = []
        self._curso = curso
    
    @property
    def curso(self):
        return self._curso
    
    @curso.setter
    def curso(self, novo_curso):
        self._curso = novo_curso

    def add_curso(self, curso):
        self.cursos_oficiais.append(curso)

aluno = Aluno('Joaquim', date(2008, 5, 10), 'Ciência de Dados')

print(f'Nome: {aluno._nome}')
print(f'Nascimento: {aluno.nascimento}')
print(f'Idade: {aluno.idade}')
print(f'Curso atual: {aluno.curso}')

aluno.curso = 'Ciência da Computação'

print(f'Novo curso: {aluno.curso}')

aluno.add_curso('Python')
aluno.add_curso('SQL')
aluno.add_curso('Power BI')

print(f'Cursos oficiais: {aluno.cursos_oficiais}')