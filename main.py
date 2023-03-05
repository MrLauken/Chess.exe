import pygame
from pygame.locals import *
import chess
from UI import *
from Leelachess import *

def main():
    pygame.init()
    pygame.display.set_caption('Chess.exe')
    win1 = pygame.display.set_mode((500, 500))
    Ai = AiActivate(win1)
    turn=1
    Lastclick= 0
    running = True
    board = chess.Board()
    Chessboard(win1)
    white_pieces(win1)
    black_pieces(win1)
    pygame.display.flip()
    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                Lastclick = event.pos
                pos1=tiles(Lastclick)


                if turn ==1:
                    if Ai == "White":
                        print(get_lcz_move(board))
                        turn = 2
                    else:
                        for i in white_pieces(screen):
                            if i.collidepoint(Lastclick):
                                indeks = white_pieces(screen).index(i)
                                turn = HRepos(indeks, turn, pos1, board)

                            
                if turn ==2:
                    if Ai == "Black":
                        print(get_lcz_move(board))
                        turn = 1
                    else: 
                        for i in black_pieces(screen):
                            if i.collidepoint(Lastclick):
                                indeks = black_pieces(screen).index(i)
                                turn = BRepos(indeks, turn, pos1, board)
                                
            
    pygame.quit()

if __name__ == "__main__":
    main()

