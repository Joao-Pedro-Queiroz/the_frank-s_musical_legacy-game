import pygame
from classes_telas import RoomBegin, RoomBoss1, RoomBoss2, RoomBoss3, RoomFinal, TelaInicial

class Jogo:
    def __init__(self):

        #teste de branch

        pygame.init()
        self.window = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('No Name') # Define o título da janela

        self.assets = {
            'fonte_padrao': pygame.font.get_default_font()
        }
        self.state = {
            'tela_atual': 0,
            'tela_dimen': (1200, 800),
            'main_clock': pygame.time.Clock(),
            'mov_jogador': [],
            }
        
        self.telas = [RoomBegin(self.state['tela_dimen']), RoomBoss1(self.state['tela_dimen']), RoomBoss2(self.state['tela_dimen']), RoomBoss3(self.state['tela_dimen']), RoomFinal(self.state['tela_dimen'])]


    def game_loop(self):

        self.state
        self.assets

        rodando = True

        tela_atual = self.telas[self.state['tela_atual']]

        while rodando:

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.k_w:
                        self.state['mov_jogador']. append('foward')
                    if event.key == pygame.k_a:
                        self.state['mov_jogador'].append('left')
                    if event.key == pygame.k_s:
                        self.state['mov_jogador'].append('back')
                    if event.key == pygame.k_d:
                        self.state['mov_jogador'].append('right')
                if event.type == pygame.KEYUP:
                    if event.key == pygame.k_w:
                        self.state['mov_jogador'].remove('foward')
                    if event.key == pygame.k_a:
                        self.state['mov_jogador'].remove('left')
                    if event.key == pygame.k_s:
                        self.state['mov_jogador'].remove('back')
                    if event.key == pygame.k_d:
                        self.state['mov_jogador'].remove('right')

            self.indice_tela_atual = tela_atual.atualiza_estado()

            self.estado['clock'].tick(60)

            if self.indice_tela_atual == -1:
                rodando = False
            else:
                tela_atual = self.telas[self.indice_tela_atual]
                tela_atual.desenha(self.window)