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

        self.x_bala = float(self.rect.x)
        self.y_bala = float(self.rect.y)

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

        self.x_bala = self.x_bala + self.vel_x * self.clock.get_time()/1000
        self.y_bala = self.y_bala + self.vel_y * self.clock.get_time()/1000

        self.rect.x = int(self.x_bala)
        self.rect.y = int(self.y_bala)

class Tiro_boss(pygame.sprite.Sprite):
    def __init__(self, pos, assets, dimen, clock, angle):

        pygame.sprite.Sprite.__init__(self)

        self.pos = pos
        self.assets = assets
        self.dimen = dimen
        self.clock = clock
        self.angle = angle

        self.sprite = pygame.image.load("Sprites/Projectiles/Boss/1/1.png")
        self.image = pygame.transform.scale(self.sprite, (30,30))
        
        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = self.pos

        self.vel_x = 0
        self.vel_y = 0

        self.vel = 250

        self.x_bala = float(self.rect.x)
        self.y_bala = float(self.rect.y)

    def update(self):

        if self.rect.x > self.dimen[0] or self.rect.x < 0:
            self.kill()
        if self.rect.y > self.dimen[1] or self.rect.y < 0:
            self.kill()

        self.vel_x = self.vel * math.cos(math.radians(self.angle))
        self.vel_y = self.vel * math.sin(math.radians(self.angle))

        self.x_bala = self.x_bala + self.vel_x * self.clock.get_time()/1000
        self.y_bala = self.y_bala + self.vel_y * self.clock.get_time()/1000

        self.rect.x = int(self.x_bala)
        self.rect.y = int(self.y_bala)


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

class rythm():
    def __init__(self, clock, bpm, bin):

        self.clock = clock
        self.bpm = bpm
        self.bin = bin

        self.metronomo = pygame.mixer.Sound("audio/batida_metronomo.wav")

        self.vel = -(bpm//6)

        self.tolerance = 20

        self.spacing = 100

        self.main_bar = pygame.Rect(self.tolerance*(-1), 0, self.tolerance*2, 30)

        self.bars = []

        for i, boolean in enumerate(bin):
            i += 1

            if boolean == '1':
                self.bars.append([self.tolerance + (i*self.spacing), 0])

        self.end = self.spacing * (len(bin)-1)

        self.toca_uma_vez = True

        self.bpm = 0

        self.cronometro = 0

        self.p_input = 0

        self.acertou_ritmo = 0

        self.errado = False
        self.dentro_do_tempo = True

    def update(self):

        self.errado = False
        self.dentro_do_tempo = False
        
        self.teclas = pygame.key.get_pressed()

        if self.teclas[pygame.K_SPACE]:
            self.p_input += 1
        else:
            self.p_input = 0

        for i in range(len(self.bars)):
            self.bars[i][0] = self.bars[i][0] + self.vel * self.clock.get_time()/100
            if self.bars[i][0] < (self.spacing) * (-1):
                self.bars[i][0] = self.end
                self.acerta_uma_vez = True
            if self.main_bar.collidepoint(self.bars[i]):
                self.dentro_do_tempo = True
                if self.p_input == 1 and self.acerta_uma_vez:
                    self.acertou_ritmo += 1
                    self.acerta_uma_vez = False
                elif self.p_input == 1:
                    self.errado = True
        
        if self.p_input == 1 and not self.dentro_do_tempo:
            self.errado = True
        
        if self.errado:
            self.acertou_ritmo = 0
        
        print(self.acertou_ritmo)

                

class UI():
    def __init__(self, player, boss, index_boss):

        self.player = player
        self.boss = boss

        self.barra_de_vida = pygame.image.load("Sprites/UI/health_bar.png")
        self.barra_de_vida_boss = pygame.image.load(f"Sprites/UI/health_bar_boss{index_boss}.png")

        self.barra_de_vida = pygame.transform.scale_by(self.barra_de_vida, 6)
        self.barra_de_vida_boss = pygame.transform.scale_by(self.barra_de_vida_boss, 6)

        self.vida = pygame.Rect(1300, 920, 250, 35)
        self.vida_boss = pygame.Rect(604, 108, 402, 50)

    def update(self):
        self.vida.w = int(self.player.hp * 5)
        self.vida_boss.w = int(self.boss.hp * 0.4 + 2)

    def draw(self, window):

        pygame.draw.rect(window, (195,0,0), self.vida)
        pygame.draw.rect(window, (255,0,0), self.vida_boss)

        window.blit(self.barra_de_vida, (1275, 900))
        window.blit(self.barra_de_vida_boss, (550, 80))



