import pygame
import math

def movimenta_player(x, y, vel_x, vel_y, clock):
        '''
        Função que realiza a movimentação do jogador

        parâmetro x: representa a poxição x do jogador
        parâmetro y: representa a poxição y do jogado
        parâmetro vel_x: representa a velocidade x do jogador
        parâmetro vel_y: representa a velocidade y do jogador
        parâmetro clock: representa o tempo dos frames
        '''

        pos_antiga = [x,y]
        vel = [vel_x, vel_y]
        pos_nova = [0,0]
        for i in range(2):
            pos_nova[i] = pos_antiga[i] + vel[i] * clock.get_time()/1000
        return pos_nova

def player_facing(angle):
    '''
        Função que define a direção do rosto do jogador

        parâmetro angle: representa o ângulo de visão do jogador
        '''

    angle = int(angle)

    directions = {
    'Forward-right': (22, 67),
    'Forward': (67, 112),
    'Forward-left': (112, 157),
    'Left': (157, 202),
    'Back-left': (202, 247),
    'Back': (247, 292),
    'Back-right': (292, 337),
    'Right': (337, 22),
    }

    for direction, rng in directions.items():
        if angle in range(0, 22) or angle in range(337, 361):
            return 'Right'
        if angle in range(rng[0], rng[1]):
            return direction


class Jogador(pygame.sprite.Sprite):

    def __init__(self, assets, clock):
        '''
        Função que define a classe Jogador

        parâmetro self: representa a própria classe
        parâmetro dimen: representa as dimensões da tela
        parâmetro clock: representa o tempo dos frames
        paràmetro assets: dicionário com alguns valores importantes para o jogo
        '''

        pygame.sprite.Sprite.__init__(self)

        self.clock = clock
        self.assets = assets

        self.sprite = pygame.image.load(r"Sprites\Player\Standing\Back\1.png")

        self.image = pygame.transform.scale_by(self.sprite, 6)

        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = [100,100]

        self.vel_x = 0
        self.vel_y = 0
        self.mov_player = []

        self.state = "Standing"
        self.facing = 'Back'

        self.frame = 0
        self.max_frames = 4
        self.animation = 0

        self.hp = 50
        
    def update(self):
        '''
        Função que atualiza o jogador

        parâmetro self: representa a própria classe
        '''

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.mov_player.append('forward')
                if event.key == pygame.K_a:
                    self.mov_player.append('left')
                if event.key == pygame.K_s:
                    self.mov_player.append('back')
                if event.key == pygame.K_d:
                    self.mov_player.append('right')
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.mov_player.remove('forward')
                if event.key == pygame.K_a:
                    self.mov_player.remove('left')
                if event.key == pygame.K_s:
                    self.mov_player.remove('back')
                if event.key == pygame.K_d:
                    self.mov_player.remove('right')

        self.rect.x, self.rect.y = movimenta_player(self.rect.x, self.rect.y, self.vel_x, self.vel_y, self.clock)

        self.vel_y = 0
        self.vel_x = 0
        
        if 'forward' in self.mov_player: self.vel_y = -250
        if 'back' in self.mov_player: self.vel_y = 250
        if 'right' in self.mov_player: self.vel_x = 250
        if 'left' in self.mov_player: self.vel_x = -250

        if 'forward' in self.mov_player and 'back' in self.mov_player:
            self.vel_y = 0
        if 'left' in self.mov_player and 'right' in self.mov_player:
            self.vel_x = 0
        
        if self.vel_y != 0 or self.vel_x != 0:
            newstate = 'Walking'
            self.max_frames = 6
        else:
            newstate = 'Standing'
            self.max_frames = 4
        
        if self.state != newstate:
            self.frame = 0
            self.animation = 0
        self.state = newstate

        # Ângulo de rotação em relação ao mouse

        image_center = ((self.rect.x + self.image.get_width()//2), (self.rect.y + self.image.get_height()//2))

        x_dist = pygame.mouse.get_pos()[0] - image_center[0]
        y_dist = pygame.mouse.get_pos()[1] - image_center[1]

        angle = math.degrees(math.atan2(y_dist, -x_dist)) + 180

        self.facing = player_facing(angle)

        # Animação do personagem

        self.animation += self.clock.get_time()
        self.frame = self.animation//150
        self.frame = (self.frame % self.max_frames) + 1

        self.personagem = pygame.image.load(f"Sprites/Player/{self.state}/{self.facing}/{self.frame}.png")
        self.image  = pygame.transform.scale_by(self.personagem, 6)

        if self.hp <= 0:
            return False
        return True

    def colide_com_tiros(self, tiros):
        '''
        Função que verifica a colisão do jogador com um tiro do boss 

        parâmetro self: representa a própria classe
        paràmetro tiros: representa a lista de tiros que será testada a colisão
        '''
        colisoes = pygame.sprite.spritecollide(self, tiros, True)
        for i in colisoes:
            self.hp -= 5
        return
        
        

class Boss1(pygame.sprite.Sprite):
    def __init__(self, dimen, clock, assets):
        '''
        Função que define a classe Boss1

        parâmetro self: representa a própria classe
        parâmetro dimen: representa as dimensões da tela
        parâmetro clock: representa o tempo dos frames
        paràmetro assets: dicionário com alguns valores importantes para o jogo
        '''

        pygame.sprite.Sprite.__init__(self)

        self.largura_tela = dimen[0]
        self.altura_tela = dimen[1]

        self.clock = clock
        self.assets = assets

        self.hp = 1000

        self.sprite = pygame.image.load("Sprites/Bosses/Boss1/1.png")
        self.image = pygame.transform.scale_by(self.sprite, 5)

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = (200, 200)

        self.tiro = [False, False]
        self.cd = 0
        self.contagem = 0

        self.animation = 0
        self.frame = 0
        self.max_frames = 4

        self.teste = pygame.Rect(self.rect.x + self.rect.w/100 * 29, self.rect.y + self.rect.h/100 * 77.5, 1,1)

        self.vivo = True

    def update(self):
        '''
        Função que atualiza o Boss1

        parâmetro self: representa a própria classe
        '''
        self.tiro = [False, False]

        self.cd += self.clock.get_time()/1000

        if self.cd >= 6:
            if self.contagem == 0:
                self.tiro = [True, False]
                self.contagem += 1
            elif self.contagem == 1:
                self.tiro = [False, True]
                self.contagem += 1
            elif self.contagem == 2:
                self.tiro = [True, True]
                self.contagem = 0
            self.cd = 0
            
        self.animation += self.clock.get_time()
        self.frame = self.animation//150
        self.frame = (self.frame % self.max_frames) + 1

        self.personagem = pygame.image.load(f"Sprites/Bosses/Boss1/{self.frame}.png")
        self.image = pygame.transform.scale_by(self.personagem, 5)

    def colide_com_tiros(self, boss, tiros):
        '''
        Função que verifica a colisão de um boss com um tiro 

        parâmetro self: representa a própria classe
        parâmetro boss: representa o chefão que será testada a colisão
        paràmetro tiros: representa a lista de tiros que será testada a colisão
        '''

        colisoes = pygame.sprite.groupcollide(boss, tiros, False, True)
        for i in colisoes.values():
            self.hp -= 5
        if self.hp <= 0:
            self.kill()
            self.vivo = False
            return False
        return True
    

class Heli(pygame.sprite.Sprite):
    def __init__(self, clock, pos):
        '''
        Função que define a classe Heli

        parâmetro self: representa a própria classe
        parâmetro clock: representa o tempo dos frames
        paràmetro pos: representa a posição do helicóptero
        '''
        pygame.sprite.Sprite.__init__(self)

        self.frames = []
        for i in range(8):
            sprite = pygame.image.load(f"Sprites/Bosses/Boss1/Heli/{i + 1}.png")

            self.frames.append(pygame.transform.scale_by(sprite, 2.5))
        
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.clock = clock
        self.rect.x, self.rect.y = pos
        self.frame = 0
        self.cronometro = 0
        self.max_frames = 7

    def update(self):
        '''
        Função que atualiza o Heli

        parâmetro self: representa a própria classe
        '''

        self.cronometro += self.clock.get_time()
        self.frame = self.cronometro//100
        self.frame = (self.frame % self.max_frames) + 1

        self.image = self.frames[self.frame]

        

class Boss2:
    def __init__(self, dimen, clock, assets):
        '''
        Função que define a classe Boss2

        parâmetro self: representa a própria classe
        parâmetro dimen: representa as dimensões da tela
        parâmetro clock: representa o tempo dos frames
        paràmetro assets: dicionário com alguns valores importantes para o jogo
        '''

        self.largura_tela = dimen[0]
        self.altura_tela = dimen[1]


class Boss3:
    def __init__(self, dimen, clock, assets):
        '''
        Função que define a classe Boss3

        parâmetro self: representa a própria classe
        parâmetro dimen: representa as dimensões da tela
        parâmetro clock: representa o tempo dos frames
        paràmetro assets: dicionário com alguns valores importantes para o jogo
        '''

        self.largura_tela = dimen[0]
        self.altura_tela = dimen[1]