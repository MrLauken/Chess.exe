import chess.engine
import pygame
from pygame.locals import *

def get_lcz_move(board):
    engine = chess.engine.SimpleEngine.popen_uci(r"C:\Users\henri\Desktop\Chess.exe\lc0-v0.29.0-windows-gpu-nvidia-cuda/lc0")  # replace with actual path to lc0 executable
    result = engine.play(board, chess.engine.Limit(time=2.0))  # 2-second time limit
    engine.quit()
    return result.move

def AiActivate(win1):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        win1.fill((100, 100, 100))
        pygame.draw.rect(win1, (245, 220, 170), pygame.Rect(10, 200, 160, 250))
        pygame.draw.rect(win1, (200, 220, 170), pygame.Rect(170, 200, 160, 250))
        pygame.draw.rect(win1, (100, 220, 170), pygame.Rect(330, 200, 160, 250))
        pygame.display.update()

