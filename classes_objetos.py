import pygame

class Tiro:
    def __init__(self, state, assets):
        self.largura_tela = state['tela_dimen'][0]
        self.altura_tela = state['tela_dimen'][1]
        

    def atualiza_estado(self):

    
    def desenha(self, window):


class Paredes:
    def __init__(self, state, assets):
        self.largura_tela = state['tela_dimen'][0]
        self.altura_tela = state['tela_dimen'][1]
        self.pos_paredes_contorno = []

        for pos_x in range(self.largura_tela):
            self.pos_paredes_contorno.append([pos_x, 0])
            self.pos_paredes_contorno.append([pos_x, self.altura_tela])

        for pos_y in range(self.altura_tela):
            self.pos_paredes_contorno.append([0, pos_y])
            self.pos_paredes_contorno.append([self.largura_tela, pos_y])
        

    def atualiza_estado(self):

    
    def desenha_paredes_contorno(self, window):


class Hazzard:
    def __init__(self, state, assets):
        self.largura_tela = state['tela_dimen'][0]
        self.altura_tela = state['tela_dimen'][1]
        

    def atualiza_estado(self):

    
    def desenha(self, window):
