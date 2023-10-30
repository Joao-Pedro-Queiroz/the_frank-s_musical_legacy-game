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

class Parede(pygame.sprite.Sprite):
    def __init__(sel):
        '''
        Função que define a classe Jogo

        parâmetro self: representa a própria classe
        ''' 

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