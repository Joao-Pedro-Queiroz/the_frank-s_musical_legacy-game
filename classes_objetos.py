import pygame

class Tiro(pygame.sprite.Sprite):
    def __init__(self, dimen, clock, assets):
        '''
        Função que define a classe Tiro

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
    def __init__(self, pos_x, pos_y, largura, altura):
        '''
        Função que define a classe Parede

        parâmetro self: representa a própria classe
        parâmetro pos_x: representa a posição x do nato superior esquerdo da parede
        parâmetro pos_y: representa a posição y do nato superior esquerdo da parede
        parâmetro largura: representa a largura da parede
        parâmetro altura: representa a altura da parede
        ''' 
    
        pygame.sprite.Sprite.__init__(self)

        self.rect = pygame.Rect(pos_x, pos_y, largura, altura)
        

    def update(self):
        pass
    
    def desenha_paredes_contorno(self, window):
        pass

class Hazzard(pygame.sprite.Sprite):
    def __init__(self, dimen, clock, assets):
        '''
        Função que define a classe Hazzard

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