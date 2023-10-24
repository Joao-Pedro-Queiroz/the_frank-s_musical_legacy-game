import pygame
from classes_telas import RoomBegin, RoomBoss1, RoomBoss2, RoomBoss3, RoomFinal, TelaInicial

class Jogo:
    def __init__(self):
        pygame.init()
        self.largura_tela = 1200
        self.altura_tela = 800
        self.fonte_padrao = pygame.font.get_default_font() # Carrega a fonte padrão
        self.window = pygame.display.set_mode((self.largura_tela, self.altura_tela))
        pygame.display.set_caption('No Name') # Define o título da janela
        self.indice_tela_atual = 0
        self.modo_ritimado = False
        self.telas = [TelaInicial(self.largura_tela, self.altura_tela), RoomBegin(self.largura_tela, self.altura_tela), RoomBoss1(self.largura_tela, self.altura_tela), RoomBoss2(self.largura_tela, self.altura_tela), RoomBoss3(self.largura_tela, self.altura_tela), RoomFinal(self.largura_tela, self.altura_tela)]


    def game_loop(self):
        tela_atual = self.telas[self.indice_tela_atual]

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