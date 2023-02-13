import pygame
from pygame.locals import *
import chess
from UI import *

def main():
    turn=1
    Lastclick= 0
    pygame.init()
    screen = pygame.display.set_mode([500, 500])
    pygame.display.set_caption('Chess.exe')
    running = True
    board = chess.Board()
    Chessboard(screen)
    white_pieces(screen)
    black_pieces(screen)
    pygame.display.flip()
    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                Lastclick = event.pos
                pos1=tiles(Lastclick)
                if turn ==1:
                    for i in white_pieces(screen):
                        if i.collidepoint(Lastclick):
                            indeks = white_pieces(screen).index(i)
                            turn = HRepos(indeks, turn, pos1, board)

                            
                if turn ==2:
                    for i in black_pieces(screen):
                        if i.collidepoint(Lastclick):
                            indeks = black_pieces(screen).index(i)
                            turn = BRepos(indeks, turn, pos1, board)

    pygame.quit()

if __name__ == "__main__":
    main()

