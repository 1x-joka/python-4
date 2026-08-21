from rich import print, inspect
from aluno import Aluno
from professor import Professor
from funcionario import Funcionario

def main():
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

if __name__ == '__main__':
    main()