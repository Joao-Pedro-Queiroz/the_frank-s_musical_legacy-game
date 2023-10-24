import pygame
from classes_personagens import Jogador, Boss1, Boss2, Boss3
from classes_objetos import Lava, Parede, Veneno, MateriaEscura

class RoomBegin:
    def __init__(self, largura_tela, altura_tela):
        self.largura_tela = largura_tela
        self.aktura_tela = altura_tela


    def atualiza_estado(self):
        for event in pygame.event.get(): # Retorna uma lista com todos os eventos que ocorreram desde a última vez que essa função foi chamada
            if event.type == pygame.QUIT: 
                return -1
            
        return 0

    
    def desenha(self, window):
        window.fill((0, 0, 0)) # Prrenche a janela do jogo com a cor preta

        pygame.display.update() # Atualiza a janela do jogo


class RoomBoss1:
    def __init__(selfself, largura_tela, altura_tela):
        self.largura_tela = largura_tela
        self.aktura_tela = altura_tela):
        

    def atualiza_estado(self):
        for event in pygame.event.get(): # Retorna uma lista com todos os eventos que ocorreram desde a última vez que essa função foi chamada
            if event.type == pygame.QUIT: 
                return -1
            
        return 1

    
    def desenha(self, window):
        window.fill((0, 0, 0)) # Prrenche a janela do jogo com a cor preta

        pygame.display.update() # Atualiza a janela do jogo


class RoomBoss2:
    def __init__(self, largura_tela, altura_tela):
        self.largura_tela = largura_tela
        self.aktura_tela = altura_tela):
        

    def atualiza_estado(self):
        for event in pygame.event.get(): # Retorna uma lista com todos os eventos que ocorreram desde a última vez que essa função foi chamada
            if event.type == pygame.QUIT: 
                return -1
            
        return 2

    
    def desenha(self, window):
        window.fill((0, 0, 0)) # Prrenche a janela do jogo com a cor preta

        pygame.display.update() # Atualiza a janela do jogo


class RoomBoss3:
    def __init__(self, largura_tela, altura_tela):
        self.largura_tela = largura_tela
        self.aktura_tela = altura_tela):
        

    def atualiza_estado(self):
        for event in pygame.event.get(): # Retorna uma lista com todos os eventos que ocorreram desde a última vez que essa função foi chamada
            if event.type == pygame.QUIT: 
                return -1
            
        return 3

    
    def desenha(self, window):
        window.fill((0, 0, 0)) # Prrenche a janela do jogo com a cor preta

        pygame.display.update() # Atualiza a janela do jogo


class RoomFinal:
    def __init__(self, largura_tela, altura_tela):
        self.largura_tela = largura_tela
        self.aktura_tela = altura_tela):
        

    def atualiza_estado(self):
        for event in pygame.event.get(): # Retorna uma lista com todos os eventos que ocorreram desde a última vez que essa função foi chamada
            if event.type == pygame.QUIT: 
                return -1
            
        return 4

    
    def desenha(self, window):
        window.fill((0, 0, 0)) # Prrenche a janela do jogo com a cor preta

        pygame.display.update() # Atualiza a janela do jogo