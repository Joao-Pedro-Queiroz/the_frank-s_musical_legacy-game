import pygame
from classes_telas import RoomBegin, RoomBoss1, RoomBoss2, RoomBoss3, RoomFinal, TelaInicial

class Jogo:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('No Name') # Define o título da janela

        self.assets = {
            'fonte_padrao': pygame.font.get_default_font()
        }
        self.state = {
            'tela_atual': 0,
            'tela_dimen': (1200, 800),
            'main_clock': pygame.time.Clock()
            }
        
        self.telas = [TelaInicial(self.state['tela_dimen']), RoomBegin(self.state['tela_dimen']), RoomBoss1(self.state['tela_dimen']), RoomBoss2(self.state['tela_dimen']), RoomBoss3(self.state['tela_dimen']), RoomFinal(self.state['tela_dimen'])]


    def game_loop(self):
        tela_atual = self.telas[self.state['tela_atual']]

        rodando = True
        while rodando:
            if self.indice_tela_atual == 0:
                self.indice_tela_atual,  self.modo_ritimado = tela_atual.atualiza_estado()
            else:
                self.indice_tela_atual = tela_atual.atualiza_estado()

            if self.indice_tela_atual == -1:
                rodando = False
            else:
                tela_atual = self.telas[self.indice_tela_atual]
                tela_atual.desenha(self.window)