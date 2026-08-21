# Crie a classe ControleRemoto, onde vamos simular o funcionamento de um controle simples (canal, volume e liga desliga)

class ControleRemoto():
    def __init__(self, canal='<desconhecido>', volume_atual = 0, ligar = False):
        self.canal = canal
        self.volume_atual = volume_atual
        self.ligar = ligar

    def mudarCanal(self, canal):
        self.canal = canal
        print(f'O canal atual é o {self.canal}')
    
    def volume_mais(self):
        self.volume_atual += 1
        print(f'Aumentando o volume..')
        print(f'Volume atual é o {self.volume_atual}')
    
    def volume_menos(self):
        self.volume_atual -= 1
        print(f'Diminuindo o volume..')
        print(f'Volume atual é o {self.volume_atual}')

    def ligando(self):
        if (self.ligar):
            print('Já está ligado!')
        else:
            self.ligar = True
            print('Ligando..')
    
    def desligando(self):
        if not (self.ligar):
            print('Já está desligado!')
        else:
            self.ligar = False
            print('Desligando..')

acao = ControleRemoto(False, False, False)
acao.ligando()
acao.ligando()
acao.mudarCanal('Master Chef')
acao.desligando()
acao.desligando()