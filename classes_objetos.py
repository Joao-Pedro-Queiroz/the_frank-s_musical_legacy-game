import pygame

class Tiro(pygame.sprite.Sprite):
    def __init__(self, dimen, clock, assets):
        '''
        Função que define a classe Jogo

        parâmetro self: representa a própria classe
        parâmetro dimen: representa as dimensões da tela
        parâmetro clock: representa o tempo dos frames
        paràmetro assets: dicionário com alguns valores importantes para o jogo
        '''

        self.largura_tela = dimen[0]
        self.altura_tela = dimen[1]
        

    def atualiza_estado(self):
        pass
    
    def desenha(self, window):
        pass

class Paredes(pygame.sprite.Sprite):
    def __init__(self, dimen, clock, assets):
        '''
        Função que define a classe Jogo

        parâmetro self: representa a própria classe
        parâmetro dimen: representa as dimensões da tela
        parâmetro clock: representa o tempo dos frames
        paràmetro assets: dicionário com alguns valores importantes para o jogo
        '''

        self.largura_tela = dimen[0]
        self.altura_tela = dimen[1]
        self.pos_paredes_contorno = []

        for pos_x in range(self.largura_tela):
            self.pos_paredes_contorno.append([pos_x, 0])
            self.pos_paredes_contorno.append([pos_x, self.altura_tela])

        for pos_y in range(self.altura_tela):
            self.pos_paredes_contorno.append([0, pos_y])
            self.pos_paredes_contorno.append([self.largura_tela, pos_y])
        

    def atualiza_estado(self):
        pass
    
    def desenha_paredes_contorno(self, window):
        pass

class Hazzard(pygame.sprite.Sprite):
    def __init__(self, dimen, clock, assets):
        '''
        Função que define a classe Jogo

        parâmetro self: representa a própria classe
        parâmetro dimen: representa as dimensões da tela
        parâmetro clock: representa o tempo dos frames
        paràmetro assets: dicionário com alguns valores importantes para o jogo
        '''

        self.largura_tela = dimen[0]
        self.altura_tela = dimen[1]
        

    def atualiza_estado(self):
        pass
    
    def desenha(self, window):
        pass