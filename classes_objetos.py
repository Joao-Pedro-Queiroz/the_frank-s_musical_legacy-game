import pygame
import math

class Tiro(pygame.sprite.Sprite):
    def __init__(self, player, assets, dimen, clock):
        '''
        Função que define a classe Jogo

        parâmetro self: representa a própria classe
        parâmetro dimen: representa as dimensões da tela
        parâmetro clock: representa o tempo dos frames
        paràmetro assets: dicionário com alguns valores importantes para o jogo
        '''

        self.clock = clock

        pygame.sprite.Sprite.__init__(self)

        self.assets = assets
        self.vel = 650

        self.tiro = pygame.image.load("Sprites/Projectiles/1/2.png")
        self.image = pygame.transform.scale_by(self.tiro, 5)
        self.rect = self.image.get_rect()

        self.largura_tela = dimen[0]
        self.altura_tela = dimen[1]

        self.player = player.rect

        center_pos = [self.player.x + (self.player.width/4), self.player.y + self.player.h/4]

        self.rect.x = center_pos[0]
        self.rect.y = center_pos[1]

        x_dist = pygame.mouse.get_pos()[0] - center_pos[0]
        y_dist = pygame.mouse.get_pos()[1] - center_pos[1]

        self.angle = math.degrees(math.atan2(y_dist, x_dist))


    def update(self):

        

        self.vel_x = self.vel * math.cos(math.radians(self.angle))
        self.vel_y = self.vel * math.sin(math.radians(self.angle))

        self.rect.x = self.rect.x + self.vel_x * self.clock.get_time()/1000
        self.rect.y = self.rect.y + self.vel_y * self.clock.get_time()/1000
    

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