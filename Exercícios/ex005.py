# Crie a classe Gamer, onde podemos cadastrar nome, nick e os jogos favoritos de uma pessoa. Crie também um método que permita mostrar a ficha desse gamer

class Gamer():
    def __init__(self, nome = '<desconhecido>', nick = '<desconhecido>', jogos_fav = []):
        self.nome = nome
        self.nick = nick
        self.jogos_fav = jogos_fav

    def addJogo(self, jogos):
        self.jogos_fav.append(jogos)
    
    def mensagem(self):
        print(f'Nome: {self.nome}')
        print(f'Nick: {self.nick}')
        print(f'Jogos Favoritos: {self.jogos_fav}')


gamer1 = Gamer('Joaquim', '1xjoka')
gamer1.addJogo('God of War III')
gamer1.addJogo('The Last of Us Part 1 Remake')
gamer1.mensagem()