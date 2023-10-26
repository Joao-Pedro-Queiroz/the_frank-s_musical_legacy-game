import pygame
import math

def movimenta_player(x, y, vel_x, vel_y, clock):
        pos_antiga = [x,y]
        vel = [vel_x, vel_y]
        pos_nova = [0,0]
        for i in range(2):
            pos_nova[i] = pos_antiga[i] + vel[i] * clock.get_time()/1000
        return pos_nova

def player_facing(angle):

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

        pygame.sprite.Sprite.__init__(self)

        self.pos = (0,0)

        self.clock = clock
        self.assets = assets

        self.personagem = pygame.image.load(r"Sprites\Player\Standing\Back\1.png")

        self.image = pygame.transform.scale_by(self.personagem, 10)

        self.rect = self.image.get_rect(center = self.pos)

        self.vel_x = 0
        self.vel_y = 0
        self.mov_player = []

        self.state = "Standing"
        self.facing = 'Back'

        self.frame = 0
        self.max_frames = 4
        self.animation = 0
        
    def update(self):

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

        
        



        




        
            


class Boss1:
    def __init__(self, state, assets):
        self.largura_tela = state['tela_dimen'][0]
        self.altura_tela = state['tela_dimen'][1]
        
class Boss2:
    def __init__(self, state, assets):
        self.largura_tela = state['tela_dimen'][0]
        self.altura_tela = state['tela_dimen'][1]

class Boss3:
    def __init__(self, state, assets):
        self.largura_tela = state['tela_dimen'][0]
        self.altura_tela = state['tela_dimen'][1]