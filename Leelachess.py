import chess.engine
import pygame
from pygame.locals import *

def get_lcz_move(board, Quit):
    engine = chess.engine.SimpleEngine.popen_uci(r"C:\Users\henri\Desktop\Chess.exe\lc0-v0.29.0-windows-gpu-nvidia-cuda/lc0")  
    result = engine.play(board, chess.engine.Limit(time=2.0))  # 2-second time limit
    engine.quit()
    return result.move
        

def layout(win1):
    win1.fill((245, 220, 170))
    SingleplayerWhite = pygame.draw.rect(win1, (200, 220, 170), pygame.Rect(10, 200, 480, 100))
    SingleplayerBlack = pygame.draw.rect(win1, (155, 220, 170), pygame.Rect(10, 300, 480, 100))
    Multiplayer = pygame.draw.rect(win1, (110, 220, 170), pygame.Rect(10, 400, 480, 100))
    display_surface = win1
    font = pygame.font.Font('freesansbold.ttf', 75)
    text = font.render('Gamemode', True, (0, 0, 0))
    display_surface.blit(text, (35, 50))

    font = pygame.font.Font('freesansbold.ttf', 50)
    singleplayer1 = font.render('Singleplayer white', True, (0,0,0))
    display_surface.blit(singleplayer1, (15, 230))

    font = pygame.font.Font('freesansbold.ttf', 50)
    singleplayer2 = font.render('Singleplayer black', True, (0,0,0))
    display_surface.blit(singleplayer2, (15, 330))

    font = pygame.font.Font('freesansbold.ttf', 50)
    Multi = font.render('Multiplayer', True, (0,0,0))
    display_surface.blit(Multi, (110, 430))

    Boxes = {"Black" : SingleplayerWhite, "White" : SingleplayerBlack, "Multiplayer" : Multiplayer}

    return Boxes


def AiActivate(win1):
    layout(win1)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                Lastclick = event.pos
                for i in layout(win1).values():
                            if i.collidepoint(Lastclick):
                                return list(layout(win1).keys())[list(layout(win1).values()).index(i)]
                            

        pygame.display.update()

