import pygame
from pygame.locals import *


def Chessboard(screen):
    n=43.5
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (245, 220, 170), pygame.Rect(30, 30, 435, 435))
    #Rad 1
    pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+n, 30+n, n, n))
    pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+2*n, 30+n, n, n))
    pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+3*n, 30+n, n, n))
    pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+4*n, 30+n, n, n))
    pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+5*n, 30+n, n, n))
    pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+6*n, 30+n, n, n))
    pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+7*n, 30+n, n, n))
    pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+8*n, 30+n, n, n))
    #Rad 2
    pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+n, 30+2*n, n, n))
    pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+2*n, 30+2*n, n, n))
    pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+3*n, 30+2*n, n, n))
    pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+4*n, 30+2*n, n, n))
    pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+5*n, 30+2*n, n, n))
    pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+6*n, 30+2*n, n, n))
    pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+7*n, 30+2*n, n, n))
    pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+8*n, 30+2*n, n, n))
    #Rad 3
    pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+n, 30+3*n, n, n))
    pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+2*n, 30+3*n, n, n))
    pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+3*n, 30+3*n, n, n))
    pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+4*n, 30+3*n, n, n))
    pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+5*n, 30+3*n, n, n))
    pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+6*n, 30+3*n, n, n))
    pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+7*n, 30+3*n, n, n))
    pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+8*n, 30+3*n, n, n))
    #Rad 4
    pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+n, 30+4*n, n, n))
    pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+2*n, 30+4*n, n, n))
    pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+3*n, 30+4*n, n, n))
    pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+4*n, 30+4*n, n, n))
    pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+5*n, 30+4*n, n, n))
    pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+6*n, 30+4*n, n, n))
    pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+7*n, 30+4*n, n, n))
    pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+8*n, 30+4*n, n, n))
    #Rad 5
    pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+n, 30+5*n, n, n))
    pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+2*n, 30+5*n, n, n))
    pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+3*n, 30+5*n, n, n))
    pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+4*n, 30+5*n, n, n))
    pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+5*n, 30+5*n, n, n))
    pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+6*n, 30+5*n, n, n))
    pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+7*n, 30+5*n, n, n))
    pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+8*n, 30+5*n, n, n))
    #Rad 6
    pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+n, 30+6*n, n, n))
    pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+2*n, 30+6*n, n, n))
    pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+3*n, 30+6*n, n, n))
    pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+4*n, 30+6*n, n, n))
    pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+5*n, 30+6*n, n, n))
    pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+6*n, 30+6*n, n, n))
    pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+7*n, 30+6*n, n, n))
    pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+8*n, 30+6*n, n, n))
    #Rad 7
    pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+n, 30+7*n, n, n))
    pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+2*n, 30+7*n, n, n))
    pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+3*n, 30+7*n, n, n))
    pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+4*n, 30+7*n, n, n))
    pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+5*n, 30+7*n, n, n))
    pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+6*n, 30+7*n, n, n))
    pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+7*n, 30+7*n, n, n))
    pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+8*n, 30+7*n, n, n))
    #Rad 8
    pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+n, 30+8*n, n, n))
    pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+2*n, 30+8*n, n, n))
    pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+3*n, 30+8*n, n, n))
    pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+4*n, 30+8*n, n, n))
    pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+5*n, 30+8*n, n, n))
    pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+6*n, 30+8*n, n, n))
    pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+7*n, 30+8*n, n, n))
    pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+8*n, 30+8*n, n, n))
    #Lines
    pygame.draw.line(screen, (164, 126, 115), (30+n,30+n), (30+n,30+9*n), 4)
    pygame.draw.line(screen, (164, 126, 115), (30+n,30+n), (30+9*n,30+n), 4)
    pygame.draw.line(screen, (164, 126, 115), (30+9*n,30+n), (30+9*n,30+9*n), 4)
    pygame.draw.line(screen, (164, 126, 115), (30+n,30+9*n), (30+9*n,30+9*n), 4)
    #Text
    display_surface = screen
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('Chess.exe', True, (164, 126, 115))
    display_surface.blit(text, (35+3*n, 35))
    #Grid numbers
    fontgrid = pygame.font.Font('freesansbold.ttf', 18)
    One = fontgrid.render('1', True, (164, 126, 115))   
    display_surface.blit(One, (n+15, 5+9*n))
    Two = fontgrid.render('2', True, (164, 126, 115))
    display_surface.blit(Two, (n+15, 5+8*n))
    Three = fontgrid.render('3', True, (164, 126, 115))
    display_surface.blit(Three, (n+15, 5+7*n))
    Four = fontgrid.render('4', True, (164, 126, 115))
    display_surface.blit(Four, (n+15, 5+6*n))
    Five = fontgrid.render('5', True, (164, 126, 115))
    display_surface.blit(Five, (n+15, 5+5*n))
    Six = fontgrid.render('6', True, (164, 126, 115))
    display_surface.blit(Six, (n+15, 5+4*n))
    Seven = fontgrid.render('7', True, (164, 126, 115))
    display_surface.blit(Seven, (n+15, 5+3*n))
    Eight = fontgrid.render('8', True, (164, 126, 115))
    display_surface.blit(Eight, (n+15, 5+2*n))
    #Grid letters
    fontgrid = pygame.font.Font('freesansbold.ttf', 18)
    A = fontgrid.render('A', True, (164, 126, 115))   
    display_surface.blit(A, (n+45, 10*n))
    B = fontgrid.render('B', True, (164, 126, 115))
    display_surface.blit(B, (n*2+45, 10*n))
    C = fontgrid.render('C', True, (164, 126, 115))
    display_surface.blit(C, (n*3+45, 10*n))
    D = fontgrid.render('D', True, (164, 126, 115))
    display_surface.blit(D, (n*4+45, 10*n))
    E = fontgrid.render('E', True, (164, 126, 115))
    display_surface.blit(E, (n*5+45, 10*n))
    F = fontgrid.render('F', True, (164, 126, 115))
    display_surface.blit(F, (n*6+45, 10*n))
    G = fontgrid.render('G', True, (164, 126, 115))
    display_surface.blit(G, (n*7+45, 10*n))
    H = fontgrid.render('H', True, (164, 126, 115))
    display_surface.blit(H, (n*8+45, 10*n))




def white_pieces(screen):
    n=43.5
    display_surface = screen

    #white rook 1
    White_rook1 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Hvit_tårn.png")
    White_rook1 = pygame.transform.scale(White_rook1, (n, n))
    display_surface.blit(White_rook1, (30+n, 30+8*n))

    #white rook 2
    White_rook2 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Hvit_tårn.png")
    White_rook2 = pygame.transform.scale(White_rook2, (n, n))
    display_surface.blit(White_rook2, (30+8*n, 30+8*n))


    #White horse 1
    White_horse1 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Hvit_hest.png")
    White_horse1 = pygame.transform.scale(White_horse1, (n, n))
    display_surface.blit(White_horse1, (30+2*n, 30+8*n))

    #White horse 2
    White_horse2 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Hvit_hest.png")
    White_horse2 = pygame.transform.scale(White_horse2, (n, n))
    display_surface.blit(White_horse2, (30+7*n, 30+8*n))

    #White bishop 1
    White_bishop1 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Hvit_biskop.png")
    White_bishop1 = pygame.transform.scale(White_bishop1, (n, n))
    display_surface.blit(White_bishop1, (30+3*n, 30+8*n))

    #White bishop 2
    White_bishop2 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Hvit_biskop.png")
    White_bishop2 = pygame.transform.scale(White_bishop2, (n, n))
    display_surface.blit(White_bishop2, (30+6*n, 30+8*n))

    #White queen
    White_queen = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Hvit_dronning.png")
    White_queen = pygame.transform.scale(White_queen, (n, n))
    display_surface.blit(White_queen, (30+4*n, 30+8*n))

    #White king
    White_king = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Hvit_konge.png")
    White_king = pygame.transform.scale(White_king, (n, n))
    display_surface.blit(White_king, (30+5*n, 30+8*n))

    #White pawn 1
    White_pawn1 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Hvit_bonde.png")
    White_pawn1 = pygame.transform.scale(White_pawn1, (n, n))
    display_surface.blit(White_pawn1, (30+n, 30+7*n))

   #White pawn 2
    White_pawn2 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Hvit_bonde.png")
    White_pawn2 = pygame.transform.scale(White_pawn2, (n, n))
    display_surface.blit(White_pawn2, (30+2*n, 30+7*n))

    #White pawn 3
    White_pawn3 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Hvit_bonde.png")
    White_pawn3 = pygame.transform.scale(White_pawn3, (n, n))
    display_surface.blit(White_pawn3, (30+3*n, 30+7*n))

    #White pawn 4
    White_pawn4 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Hvit_bonde.png")
    White_pawn4 = pygame.transform.scale(White_pawn4, (n, n))
    display_surface.blit(White_pawn4, (30+4*n, 30+7*n))

    #White pawn 5
    White_pawn5 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Hvit_bonde.png")
    White_pawn5 = pygame.transform.scale(White_pawn5, (n, n))
    display_surface.blit(White_pawn5, (30+5*n, 30+7*n))

    #White pawn 6
    White_pawn6 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Hvit_bonde.png")
    White_pawn6 = pygame.transform.scale(White_pawn6, (n, n))
    display_surface.blit(White_pawn6, (30+6*n, 30+7*n))

    #White pawn 7
    White_pawn7 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Hvit_bonde.png")
    White_pawn7 = pygame.transform.scale(White_pawn7, (n, n))
    display_surface.blit(White_pawn7, (30+7*n, 30+7*n))

    #White pawn 8
    White_pawn8 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Hvit_bonde.png")
    White_pawn8 = pygame.transform.scale(White_pawn8, (n, n))
    display_surface.blit(White_pawn8, (30+8*n, 30+7*n))

def black_pieces(screen):
    n=43.5
    display_surface = screen

    #black rook 1
    Black_rook1 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Svart_tårn.png")
    Black_rook1 = pygame.transform.scale(Black_rook1, (n, n))
    display_surface.blit(Black_rook1, (30+n, 30+n))

    #black rook 2
    Black_rook2 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Svart_tårn.png")
    Black_rook2 = pygame.transform.scale(Black_rook2, (n, n))
    display_surface.blit(Black_rook2, (30+8*n, 30+n))

    #black horse 1
    Black_horse1 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Svart_hest.png")
    Black_horse1 = pygame.transform.scale(Black_horse1, (n, n))
    display_surface.blit(Black_horse1, (30+2*n, 30+n))

    #black horse 2
    Black_horse2 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Svart_hest.png")
    Black_horse2 = pygame.transform.scale(Black_horse2, (n, n))
    display_surface.blit(Black_horse2, (30+7*n, 30+n))

    #black bishop 1
    Black_bishop1 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Svart_biskop.png")
    Black_bishop1 = pygame.transform.scale(Black_bishop1, (n, n))
    display_surface.blit(Black_bishop1, (30+3*n, 30+n))

    #black bishop 2
    Black_bishop2 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Svart_biskop.png")
    Black_bishop2 = pygame.transform.scale(Black_bishop2, (n, n))
    display_surface.blit(Black_bishop2, (30+6*n, 30+n))

    #black queen
    Black_queen = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Svart_dronning.png")
    Black_queen = pygame.transform.scale(Black_queen, (n, n))
    display_surface.blit(Black_queen, (30+4*n, 30+n))

    #black king
    Black_king = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Svart_konge.png")
    Black_king = pygame.transform.scale(Black_king, (n, n))
    display_surface.blit(Black_king, (30+5*n, 30+n))

    #black pawn 1
    Black_pawn1 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Svart_bonde.png")
    Black_pawn1 = pygame.transform.scale(Black_pawn1, (n, n))
    display_surface.blit(Black_pawn1, (30+n, 30+2*n))

    #black pawn 2
    Black_pawn2 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Svart_bonde.png")
    Black_pawn2 = pygame.transform.scale(Black_pawn2, (n, n))
    display_surface.blit(Black_pawn1, (30+2*n, 30+2*n))

    #black pawn 3
    Black_pawn3 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Svart_bonde.png")
    Black_pawn3 = pygame.transform.scale(Black_pawn1, (n, n))
    display_surface.blit(Black_pawn3, (30+3*n, 30+2*n))

    #black pawn 4
    Black_pawn4 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Svart_bonde.png")
    Black_pawn4 = pygame.transform.scale(Black_pawn1, (n, n))
    display_surface.blit(Black_pawn4, (30+4*n, 30+2*n))

    #black pawn 5
    Black_pawn5 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Svart_bonde.png")
    Black_pawn5 = pygame.transform.scale(Black_pawn1, (n, n))
    display_surface.blit(Black_pawn1, (30+5*n, 30+2*n))

    #black pawn 6
    Black_pawn6 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Svart_bonde.png")
    Black_pawn6 = pygame.transform.scale(Black_pawn1, (n, n))
    display_surface.blit(Black_pawn1, (30+6*n, 30+2*n))

    #black pawn 7
    Black_pawn7 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Svart_bonde.png")
    Black_pawn7 = pygame.transform.scale(Black_pawn7, (n, n))
    display_surface.blit(Black_pawn1, (30+7*n, 30+2*n))

    #black pawn 8
    Black_pawn8 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Svart_bonde.png")
    Black_pawn8 = pygame.transform.scale(Black_pawn8, (n, n))
    display_surface.blit(Black_pawn1, (30+8*n, 30+2*n))



             



pygame.init()

screen = pygame.display.set_mode([500, 500])

pygame.display.set_caption('Chess.exe')
 


running = True

Chessboard(screen)
white_pieces(screen)
black_pieces(screen)
pygame.display.flip()

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False


pygame.quit()