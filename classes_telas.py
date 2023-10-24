import pygame
from classes_personagens import Jogador, Boss1, Boss2, Boss3
from classes_objetos import Lava, Parede, Veneno, MateriaEscura

class RoomBegin:
    def __init__(self, state, assets):
        self.largura_tela = state['tela_dimen'][0]
        self.altura_tela = state['tela_dimen'][1]


    def atualiza_estado(self):
        for event in pygame.event.get(): # Retorna uma lista com todos os eventos que ocorreram desde a última vez que essa função foi chamada
            if event.type == pygame.QUIT: 
                return -1
            
        return 0

    
    def desenha(self, window):
        window.fill((0, 0, 0)) # Prrenche a janela do jogo com a cor preta

        pygame.display.update() # Atualiza a janela do jogo


class RoomBoss1:
    def __init__(self, state, assets):
        self.largura_tela = state['tela_dimen'][0]
        self.altura_tela = state['tela_dimen'][1]
        

    def atualiza_estado(self):
        for event in pygame.event.get(): # Retorna uma lista com todos os eventos que ocorreram desde a última vez que essa função foi chamada
            if event.type == pygame.QUIT: 
                return -1
            
        return 1

    
    def desenha(self, window):
        window.fill((0, 0, 0)) # Prrenche a janela do jogo com a cor preta

        pygame.display.update() # Atualiza a janela do jogo


class RoomBoss2:
    def __init__(self, state, assets):
        self.largura_tela = state['tela_dimen'][0]
        self.altura_tela = state['tela_dimen'][1]
        

    def atualiza_estado(self):
        for event in pygame.event.get(): # Retorna uma lista com todos os eventos que ocorreram desde a última vez que essa função foi chamada
            if event.type == pygame.QUIT: 
                return -1
            
        return 2

    
    def desenha(self, window):
        window.fill((0, 0, 0)) # Prrenche a janela do jogo com a cor preta

        pygame.display.update() # Atualiza a janela do jogo


class RoomBoss3:
    def __init__(self, state, assets):
        self.largura_tela = state['tela_dimen'][0]
        self.altura_tela = state['tela_dimen'][1]

    def atualiza_estado(self):
        for event in pygame.event.get(): # Retorna uma lista com todos os eventos que ocorreram desde a última vez que essa função foi chamada
            if event.type == pygame.QUIT: 
                return -1
            
        return 3

    
    def desenha(self, window):
        window.fill((0, 0, 0)) # Prrenche a janela do jogo com a cor preta

        pygame.display.update() # Atualiza a janela do jogo


class RoomFinal:
    def __init__(self, state, assets):
        self.largura_tela = state['tela_dimen'][0]
        self.altura_tela = state['tela_dimen'][1]
        

    def atualiza_estado(self):
        for event in pygame.event.get(): # Retorna uma lista com todos os eventos que ocorreram desde a última vez que essa função foi chamada
            if event.type == pygame.QUIT: 
                return -1
            
        return 4

    
    def desenha(self, window):
        window.fill((0, 0, 0)) # Prrenche a janela do jogo com a cor preta

        pygame.display.update() # Atualiza a janela do jogo


class TelaFinal:
    def __init__(self, state, assets):
        self.largura_tela = state['tela_dimen'][0]
        self.altura_tela = state['tela_dimen'][1]
        self.fonte_padrao = pygame.font.get_default_font()
        self.font_texto = pygame.font.Font(self.fonte_padrao, 20)

    
    def atualiza_estado(self):
        for event in pygame.event.get(): # Retorna uma lista com todos os eventos que ocorreram desde a última vez que essa função foi chamada
            if event.type == pygame.QUIT: 
                return -1
        
        return 5
            
    
    def desenha(self, window):
        window.fill((0, 0, 0)) # Prrenche a janela do jogo com a cor preta

        texto_final = self.font_texto.render(f'PARABÉNS! VOCÊ CONSEGIUI A DROGA LENDÄRIA', True, (0, 255, 0)) # Cria uma imagem do texto
        window.blit(texto_final, (self.largura_tela // 2 - 125, self.altura_tela // 2)) # Desenha a imagem já carregada por pygame.image.load em window na posição (x, y).

        pygame.display.update() # Atualiza a janela do jogo


class TelaGameOver:
    def __init__(self, state, assets):
        self.largura_tela = state['tela_dimen'][0]
        self.altura_tela = state['tela_dimen'][1]
        self.fonte_padrao = pygame.font.get_default_font()
        self.font_texto = pygame.font.Font(self.fonte_padrao, 20)
    

    def atualiza_estado(self):
        for event in pygame.event.get(): # Retorna uma lista com todos os eventos que ocorreram desde a última vez que essa função foi chamada
            if event.type == pygame.QUIT: 
                return -1
            
        return 6
        
    
    def desenha(self, window):
        window.fill((0, 0, 0))
        
        texto_morte = self.font_texto.render(f'VOCË MORREU', True, (255, 0, 0)) # Cria uma imagem do texto
        window.blit(texto_morte, (self.largura_tela // 2 - 85, self.altura_tela // 2)) # Desenha a imagem já carregada por pygame.image.load em window na posição (x, y).

        pygame.display.update()