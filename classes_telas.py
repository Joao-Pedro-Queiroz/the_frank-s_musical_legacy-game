import pygame
from classes_personagens import Jogador, Boss1, Boss2, Boss3
from classes_objetos import Lava, Parede, Veneno, MateriaEscura

class TelaInicial:
    def __init__(self, state, assets):
        self.largura_tela = state['tela_dimen'][0]
        self.altura_tela = state['tela_dimen'][1]
        self.fonte_padrao = pygame.font.get_default_font() # Carrega a fonte padrão
        self.font_texto = pygame.font.Font(self.fonte_padrao, 16)
        self.font_nome_jogo = pygame.font.Font(self.fonte_padrao, 20)
        self.ret_largura = 100
        self.ret_altura = 35
        self.ret_x = self.largura_tela // 2 - self.ret_largura // 2
        self.ret_y = self.altura_tela // 2 + self.ret_altura // 2
        self.ret_cor = (255, 0, 0)
        self.botòes = []

        for i in range(2):
            self.botòes.append([self.ret_x, self.ret_y])
            self.ret_y += 50


    def atualiza_estado(self):
        for event in pygame.event.get(): # Retorna uma lista com todos os eventos que ocorreram desde a última vez que essa função foi chamada
            if event.type == pygame.QUIT: 
                return -1, False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pass
                pos_mouse = pygame.mouse.get_pos()
                
                for indice, botão in enumerate(self.botòes):
                    rect = pygame.Rect(botão[0], botão[1], self.ret_largura, self.ret_altura)

                    if rect.collidepoint(pos_mouse) and indice == 0:
                        return 1, False
                    elif rect.collidepoint(pos_mouse) and indice == 1:
                        return 1, True
            
        return 0, False

    
    def desenha(self, window):
        window.fill((0, 0, 0)) # Prrenche a janela do jogo com a cor preta

        nome_jogo = self.font_nome_jogo.render('NOME DO JOGO', True, (0, 0, 255)) # Cria uma imagem do texto
        window.blit(nome_jogo, ( self.largura_tela // 2 - 100, self.altura_tela // 2 + 55)) # Desenha a imagem já carregada por pygame.image.load em window na posição (x, y).

        vertice_ret_1 = ((self.botòes[0][0], self.botòes[0][1]), (self.botòes[0][0] + self.ret_largura, self.botòes[0][1]), (self.botòes[0][0] + self.ret_largura, self.botòes[0][1] + self.ret_altura), (self.botòes[0][0], self.botòes[0][1] + self.ret_altura))
        pygame.draw.polygon(window, self.ret_cor, vertice_ret_1)
        texto_play1 = self.font_texto.render('JOGAR MODO NORMAL', True, (0, 0, 0)) # Cria uma imagem do texto
        window.blit(texto_play1, (self.botòes[0][0] + 5, self.botòes[0][1] + 5)) # Desenha a imagem já carregada por pygame.image.load em window na posição (x, y).

        vertice_ret_1 = ((self.botòes[1][0], self.botòes[1][1]), (self.botòes[1][0] + self.ret_largura, self.botòes[1][1]), (self.botòes[1][0] + self.ret_largura, self.botòes[1][1] + self.ret_altura), (self.botòes[1][0], self.botòes[1][1] + self.ret_altura))
        pygame.draw.polygon(window, self.ret_cor, vertice_ret_1)
        texto_play1 = self.font_texto.render('JOGAR MODO RITIMADO', True, (0, 0, 0)) # Cria uma imagem do texto
        window.blit(texto_play1, (self.botòes[1][0] + 5, self.botòes[1][1] + 5)) # Desenha a imagem já carregada por pygame.image.load em window na posição (x, y).

        pygame.display.update() # Atualiza a janela do jogo


class RoomBegin:
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


class RoomBoss1:
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


class RoomBoss2:
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


class RoomBoss3:
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


class RoomFinal:
    def __init__(self, state, assets):
        self.largura_tela = state['tela_dimen'][0]
        self.altura_tela = state['tela_dimen'][1]
        

    def atualiza_estado(self):
        for event in pygame.event.get(): # Retorna uma lista com todos os eventos que ocorreram desde a última vez que essa função foi chamada
            if event.type == pygame.QUIT: 
                return -1
            
        return 5

    
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
        
        return 6
            
    
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
            
        return 7
        
    
    def desenha(self, window):
        window.fill((0, 0, 0))
        
        texto_morte = self.font_texto.render(f'VOCË MORREU', True, (255, 0, 0)) # Cria uma imagem do texto
        window.blit(texto_morte, (self.largura_tela // 2 - 85, self.altura_tela // 2)) # Desenha a imagem já carregada por pygame.image.load em window na posição (x, y).

        pygame.display.update()