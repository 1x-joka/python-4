# Crie a classe Livro, que vai simular a passagem de páginas de um livro, considerando também se o usuário chegou ao fim da leitura

class Livro:
    def __init__(self, paginas = 0, pagina_atual = 1):
        self.paginas = paginas
        self.pagina_atual = pagina_atual

    def addPagina(self):
        if (self.pagina_atual == self.paginas):
            print('Acabou!')
        else:
            self.pagina_atual += 1
            print('Folheando uma página...')

    def remPagina(self):
        if (self.pagina_atual == 1):
            print('Você já está no início!')
        else:
            self.pagina_atual -= 1
            print('Removendo uma página...')

    def estadoAtual(self):
        return f'Sua página atual é a {self.pagina_atual}'

usuario = Livro(3) # criando um livro com 3 páginas
usuario.addPagina() # agora estou na primeira...
usuario.addPagina()
usuario.remPagina()
print(usuario.estadoAtual())