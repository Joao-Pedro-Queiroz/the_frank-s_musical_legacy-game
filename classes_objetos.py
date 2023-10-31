import pygame
import math
import random

class Tiro(pygame.sprite.Sprite):
    def __init__(self, player, assets, dimen, clock):
        '''
        Função que define a classe Tiro

        parâmetro self: representa a própria classe
        parâmetro player: representa o jogador
        parâmetro dimen: representa as dimensões da tela
        parâmetro clock: representa o tempo dos frames
        paràmetro assets: dicionário com alguns valores importantes para o jogo
        '''

        self.clock = clock

        pygame.sprite.Sprite.__init__(self)

        self.assets = assets
        self.vel = 650

        tipo = random.randint(1,4)
        cor = random.randint(1,8)

        self.tiro = pygame.image.load(f"Sprites/Projectiles/{tipo}/{cor}.png")
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
        '''
        Função que atualiza o tiro

        parâmetro self: representa a própria classe
        '''
        

        self.vel_x = self.vel * math.cos(math.radians(self.angle))
        self.vel_y = self.vel * math.sin(math.radians(self.angle))

        self.rect.x = self.rect.x + self.vel_x * self.clock.get_time()/1000
        self.rect.y = self.rect.y + self.vel_y * self.clock.get_time()/1000
    

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