import pygame
from classes_personagens import *
from classes_objetos import *

class RoomBegin:
    def __init__(self, dimen, clock, assets):
        '''
        Função que define a classe RoomBegin

        parâmetro self: representa a própria classe
        parâmetro dimen: representa as dimensões da tela
        parâmetro clock: representa o tempo dos frames
        paràmetro assets: dicionário com alguns valores importantes para o jogo
        '''
        self.largura_tela = dimen[0]
        self.altura_tela = dimen[1]

        self.dimen = dimen

        self.clock = clock
        self.assets = assets
        self.sprites = pygame.sprite.Group()
        self.tiros = pygame.sprite.Group()
        self.boss = pygame.sprite.Group()

        self.personagem = Jogador(assets, clock)
        self.sprites.add(self.personagem)
        
        self.boss1 = Boss1(self.dimen, self.clock, self.assets)
        self.boss.add(self.boss1)

        self.fire_rate = 300
        self.count_fr = 0


    def atualiza_estado(self):
        '''
        Função que atualiza a tela do RoomBegin

        parâmetro self: representa a própria classe
        '''

        for event in pygame.event.get(pygame.QUIT): # Retorna uma lista com todos os eventos que ocorreram desde a última vez que essa função foi chamada
            if event.type == pygame.QUIT: 
                return -1
            
        self.personagem.update()

        if pygame.mouse.get_pressed()[0]:
            if self.count_fr == 0:
                self.tiros.add(Tiro(self.personagem, self.assets, self.dimen, self.clock))
            self.count_fr += self.clock.get_time()
            if self.count_fr >= self.fire_rate:
                self.count_fr = 0
        else:
            self.count_fr = 0

        self.tiros.update()

        self.boss1.colide_com_tiros(self.boss1, self.tiros)

        print(self.boss1.hp)

        return 0

    
    def desenha(self, window):
        '''
        Função que desenha a tela do jogo

        parâmetro self: representa a própria classe
        parâmetro window: representa a janlea do jogo
        '''

        window.fill((0, 0, 0)) # Prrenche a janela do jogo com a cor preta

        self.tiros.draw(window)
        self.sprites.draw(window)
        self.boss.draw(window)

        pygame.display.update() # Atualiza a janela do jogo


# class RoomBoss1:
#     def __init__(self, dimen, clock, assets):
#         self.largura_tela = state['tela_dimen'][0]
#         self.altura_tela = state['tela_dimen'][1]
        

#     def atualiza_estado(self):
#         for event in pygame.event.get(): # Retorna uma lista com todos os eventos que ocorreram desde a última vez que essa função foi chamada
#             if event.type == pygame.QUIT: 
#                 return -1
            
#         return 1

    
#     def desenha(self, window):
#         window.fill((0, 0, 0)) # Preenche a janela do jogo com a cor preta

#         pygame.display.update() # Atualiza a janela do jogo


# class RoomBoss2:
#     def __init__(self, dimen, clock, assets):
#         self.largura_tela = state['tela_dimen'][0]
#         self.altura_tela = state['tela_dimen'][1]
        

#     def atualiza_estado(self):
#         for event in pygame.event.get(): # Retorna uma lista com todos os eventos que ocorreram desde a última vez que essa função foi chamada
#             if event.type == pygame.QUIT: 
#                 return -1
            
#         return 2

    
#     def desenha(self, window):
#         window.fill((0, 0, 0)) # Preenche a janela do jogo com a cor preta

#         pygame.display.update() # Atualiza a janela do jogo


# class RoomBoss3:
#     def __init__(self, dimen, clock, assets):
#         self.largura_tela = state['tela_dimen'][0]
#         self.altura_tela = state['tela_dimen'][1]

#     def atualiza_estado(self):
#         for event in pygame.event.get(): # Retorna uma lista com todos os eventos que ocorreram desde a última vez que essa função foi chamada
#             if event.type == pygame.QUIT: 
#                 return -1
            
#         return 3

    
#     def desenha(self, window):
#         window.fill((0, 0, 0)) # Preenche a janela do jogo com a cor preta

#         pygame.display.update() # Atualiza a janela do jogo


# class RoomFinal:
#     def __init__(self, dimen, clock, assets):
#         self.largura_tela = state['tela_dimen'][0]
#         self.altura_tela = state['tela_dimen'][1]
        

#     def atualiza_estado(self):
#         for event in pygame.event.get(): # Retorna uma lista com todos os eventos que ocorreram desde a última vez que essa função foi chamada
#             if event.type == pygame.QUIT: 
#                 return -1
            
#         return 4

    
#     def desenha(self, window):
#         window.fill((0, 0, 0)) # Preenche a janela do jogo com a cor preta

#         pygame.display.update() # Atualiza a janela do jogo


# class TelaFinal:
#     def __init__(self, dimen, clock, assets):
#         self.largura_tela = state['tela_dimen'][0]
#         self.altura_tela = state['tela_dimen'][1]
#         self.fonte_padrao = pygame.font.get_default_font()
#         self.font_texto = pygame.font.Font(self.fonte_padrao, 20)

    
#     def atualiza_estado(self):
#         for event in pygame.event.get(): # Retorna uma lista com todos os eventos que ocorreram desde a última vez que essa função foi chamada
#             if event.type == pygame.QUIT: 
#                 return -1
        
#         return 5
            
    
#     def desenha(self, window):
#         window.fill((0, 0, 0)) # Preenche a janela do jogo com a cor preta

#         texto_final = self.font_texto.render(f'PARABÉNS! VOCÊ CONSEGIUI A DROGA LENDÄRIA', True, (0, 255, 0)) # Cria uma imagem do texto
#         window.blit(texto_final, (self.largura_tela // 2 - 125, self.altura_tela // 2)) # Desenha a imagem já carregada por pygame.image.load em window na posição (x, y).

#         pygame.display.update() # Atualiza a janela do jogo


# class TelaGameOver:
#     def __init__(self, dimen, clock, assets):
#         self.largura_tela = state['tela_dimen'][0]
#         self.altura_tela = state['tela_dimen'][1]
#         self.fonte_padrao = pygame.font.get_default_font()
#         self.font_texto = pygame.font.Font(self.fonte_padrao, 20)
    

#     def atualiza_estado(self):
#         for event in pygame.event.get(): # Retorna uma lista com todos os eventos que ocorreram desde a última vez que essa função foi chamada
#             if event.type == pygame.QUIT: 
#                 return -1
            
#         return 6
        
    
#     def desenha(self, window):
#         window.fill((0, 0, 0)) # Preenche a janela do jogo com a cor preta

#         texto_morte = self.font_texto.render(f'VOCË MORREU', True, (255, 0, 0)) # Cria uma imagem do texto
#         window.blit(texto_morte, (self.largura_tela // 2 - 85, self.altura_tela // 2)) # Desenha a imagem já carregada por pygame.image.load em window na posição (x, y).

#         pygame.display.update()