import pygame
from pygame.locals import *
n=43.5
turn=1
Lastclick= 0


#initializerer poisisjon for hvite brikker
Wrook1pos = (30+n, 30+8*n)
Wrook2pos = (30+8*n, 30+8*n)
Whorse1pos = (30+2*n, 30+8*n)
Whorse2pos = (30+7*n, 30+8*n)
Wbishop1pos = (30+3*n, 30+8*n)
Wbishop2pos = (30+6*n, 30+8*n)
WqueenPos = (30+4*n, 30+8*n)
WkingPos = (30+5*n, 30+8*n)
Wpawn1 = (30+n, 30+7*n)
Wpawn2= (30+2*n, 30+7*n)
Wpawn3= (30+3*n, 30+7*n)
Wpawn4= (30+4*n, 30+7*n)
Wpawn5= (30+5*n, 30+7*n)
Wpawn6= (30+6*n, 30+7*n)
Wpawn7= (30+7*n, 30+7*n)
Wpawn8= (30+8*n, 30+7*n)

#initializerer poisisjon for svarte brikker
Brook1pos = (30+n, 30+n)
Brook2pos = (30+8*n, 30+n)
Bhorse1pos = (30+2*n, 30+n)
Bhorse2pos = (30+7*n, 30+n)
Bbishop1pos = (30+3*n, 30+n)
Bbishop2pos = (30+6*n, 30+n)
BqueenPos = (30+4*n, 30+n)
BkingPos = (30+5*n, 30+n)
Bpawn1 = (30+n, 30+2*n)
Bpawn2= (30+2*n, 30+2*n)
Bpawn3= (30+3*n, 30+2*n)
Bpawn4= (30+4*n, 30+2*n)
Bpawn5= (30+5*n, 30+2*n)
Bpawn6= (30+6*n, 30+2*n)
Bpawn7= (30+7*n, 30+2*n)
Bpawn8= (30+8*n, 30+2*n)

#Liste med hvits posisjoner på brettet
Hvitliste = [Wrook1pos, Wrook2pos, Whorse1pos, Whorse2pos, Wbishop1pos, Wbishop2pos, WqueenPos, WkingPos, Wpawn1, 
Wpawn2, Wpawn3, Wpawn4, Wpawn5, Wpawn6, Wpawn7, Wpawn8]


#Liste med svarts posisjoner på brettet
Bliste = [Brook1pos, Brook2pos, Bhorse1pos, Bhorse2pos, Bbishop1pos, Bbishop2pos, BqueenPos, BkingPos,
Bpawn1, Bpawn2, Bpawn3, Bpawn4, Bpawn5, Bpawn6, Bpawn7, Bpawn8]




def Chessboard(screen):
    n=43.5
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (245, 220, 170), pygame.Rect(30, 30, 435, 435))
    #Rad 8
    a8= pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+n, 30+n, n, n))
    b8= pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+2*n, 30+n, n, n))
    c8= pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+3*n, 30+n, n, n))
    d8= pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+4*n, 30+n, n, n))
    e8= pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+5*n, 30+n, n, n))
    f8= pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+6*n, 30+n, n, n))
    g8= pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+7*n, 30+n, n, n))
    h8= pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+8*n, 30+n, n, n))
    #Rad 7
    a7= pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+n, 30+2*n, n, n))
    b7= pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+2*n, 30+2*n, n, n))
    c7= pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+3*n, 30+2*n, n, n))
    d7= pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+4*n, 30+2*n, n, n))
    e7= pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+5*n, 30+2*n, n, n))
    f7= pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+6*n, 30+2*n, n, n))
    g7= pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+7*n, 30+2*n, n, n))
    h7= pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+8*n, 30+2*n, n, n))
    #Rad 6
    a6= pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+n, 30+3*n, n, n))
    b6= pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+2*n, 30+3*n, n, n))
    c6= pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+3*n, 30+3*n, n, n))
    d6= pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+4*n, 30+3*n, n, n))
    e6= pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+5*n, 30+3*n, n, n))
    f6= pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+6*n, 30+3*n, n, n))
    g6= pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+7*n, 30+3*n, n, n))
    h6= pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+8*n, 30+3*n, n, n))
    #Rad 5
    a5= pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+n, 30+4*n, n, n))
    b5= pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+2*n, 30+4*n, n, n))
    c5= pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+3*n, 30+4*n, n, n))
    d5=pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+4*n, 30+4*n, n, n))
    e5=pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+5*n, 30+4*n, n, n))
    f5=pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+6*n, 30+4*n, n, n))
    g5=pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+7*n, 30+4*n, n, n))
    h5=pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+8*n, 30+4*n, n, n))
    #Rad 4
    a4= pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+n, 30+5*n, n, n))
    b4= pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+2*n, 30+5*n, n, n))
    c4= pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+3*n, 30+5*n, n, n))
    d4= pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+4*n, 30+5*n, n, n))
    e4= pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+5*n, 30+5*n, n, n))
    f4= pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+6*n, 30+5*n, n, n))
    g4= pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+7*n, 30+5*n, n, n))
    h4= pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+8*n, 30+5*n, n, n))
    #Rad 3
    a3= pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+n, 30+6*n, n, n))
    b3= pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+2*n, 30+6*n, n, n))
    c3= pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+3*n, 30+6*n, n, n))
    d3= pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+4*n, 30+6*n, n, n))
    e3= pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+5*n, 30+6*n, n, n))
    f3= pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+6*n, 30+6*n, n, n))
    g3= pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+7*n, 30+6*n, n, n))
    h3= pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+8*n, 30+6*n, n, n))
    #Rad 2
    a2= pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+n, 30+7*n, n, n))
    b2= pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+2*n, 30+7*n, n, n))
    c2= pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+3*n, 30+7*n, n, n))
    d2= pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+4*n, 30+7*n, n, n))
    e2= pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+5*n, 30+7*n, n, n))
    f2= pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+6*n, 30+7*n, n, n))
    g2= pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+7*n, 30+7*n, n, n))
    h2= pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+8*n, 30+7*n, n, n))
    #Rad 1
    a1= pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+n, 30+8*n, n, n))
    b1= pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+2*n, 30+8*n, n, n))
    c1= pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+3*n, 30+8*n, n, n))
    d1= pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+4*n, 30+8*n, n, n))
    e1= pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+5*n, 30+8*n, n, n))
    f1= pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+6*n, 30+8*n, n, n))
    g1= pygame.draw.rect(screen, (164, 126, 115), pygame.Rect(30+7*n, 30+8*n, n, n))
    h1= pygame.draw.rect(screen, (240, 215, 185), pygame.Rect(30+8*n, 30+8*n, n, n))
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

    tiles = [a8,b8,c8,d8,e8,f8,g8,h8,a7,b7,c7,d7,e7,f7,g7,h7, a6,b6,c6,d6,e6,f6,g6,h6, a5,b5,c5,d5,e5,f5,g5,h5,
    a4,b4,c4,d4,e4,f4,g4,h4, a3,b3,c3,d3,e3,f3,g3,h3,a2,b2,c2,d2,e2,f2,g2,h2,a1,b1,c1,d1,e1,f1,g1,h1]
    return tiles




def white_pieces(screen):
    n=43.5
    
    #white rook 1
    White_rook1 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Hvit_tårn.png")
    White_rook1 = pygame.transform.scale(White_rook1, (n, n))
    White_rook1Pos= screen.blit(White_rook1, Hvitliste[0])

    #white rook 2
    White_rook2 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Hvit_tårn.png")
    White_rook2 = pygame.transform.scale(White_rook2, (n, n))
    White_rook2Pos= screen.blit(White_rook2, Hvitliste[1])

    #White horse 1
    White_horse1 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Hvit_hest.png")
    White_horse1 = pygame.transform.scale(White_horse1, (n, n))
    White_horse1Pos= screen.blit(White_horse1, Hvitliste[2])

    #White horse 2
    White_horse2 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Hvit_hest.png")
    White_horse2 = pygame.transform.scale(White_horse2, (n, n))
    White_horse2Pos= screen.blit(White_horse2, Hvitliste[3])

    #White bishop 1
    White_bishop1 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Hvit_biskop.png")
    White_bishop1 = pygame.transform.scale(White_bishop1, (n, n))
    White_bishop1Pos= screen.blit(White_bishop1, Hvitliste[4])

    #White bishop 2
    White_bishop2 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Hvit_biskop.png")
    White_bishop2 = pygame.transform.scale(White_bishop2, (n, n))
    White_bishop2Pos= screen.blit(White_bishop2, Hvitliste[5])

    #White queen
    White_queen = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Hvit_dronning.png")
    White_queen = pygame.transform.scale(White_queen, (n, n))
    White_queenPos= screen.blit(White_queen, Hvitliste[6])

    #White king
    White_king = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Hvit_konge.png")
    White_king = pygame.transform.scale(White_king, (n, n))
    White_kingPos= screen.blit(White_king, Hvitliste[7])
    

    #White pawn 1
    White_pawn1 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Hvit_bonde.png")
    White_pawn1 = pygame.transform.scale(White_pawn1, (n, n))
    White_pawn1Pos= screen.blit(White_pawn1, Hvitliste[8])
    
   #White pawn 2
    White_pawn2 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Hvit_bonde.png")
    White_pawn2 = pygame.transform.scale(White_pawn2, (n, n))
    White_pawn2Pos= screen.blit(White_pawn2, Hvitliste[9])
    

    #White pawn 3
    White_pawn3 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Hvit_bonde.png")
    White_pawn3 = pygame.transform.scale(White_pawn3, (n, n))
    White_pawn3Pos= screen.blit(White_pawn3, Hvitliste[10])

    #White pawn 4
    White_pawn4 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Hvit_bonde.png")
    White_pawn4 = pygame.transform.scale(White_pawn4, (n, n))
    White_pawn4Pos= screen.blit(White_pawn4, Hvitliste[11])

    #White pawn 5
    White_pawn5 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Hvit_bonde.png")
    White_pawn5 = pygame.transform.scale(White_pawn5, (n, n))
    White_pawn5Pos= screen.blit(White_pawn5, Hvitliste[12])

    #White pawn 6
    White_pawn6 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Hvit_bonde.png")
    White_pawn6 = pygame.transform.scale(White_pawn6, (n, n))
    White_pawn6Pos= screen.blit(White_pawn6, Hvitliste[13])

    #White pawn 7
    White_pawn7 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Hvit_bonde.png")
    White_pawn7 = pygame.transform.scale(White_pawn7, (n, n))
    White_pawn7Pos= screen.blit(White_pawn7, Hvitliste[14])

    #White pawn 8
    White_pawn8 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Hvit_bonde.png")
    White_pawn8 = pygame.transform.scale(White_pawn8, (n, n))
    White_pawn8Pos= screen.blit(White_pawn8, Hvitliste[15])


    piecelist = [White_rook1Pos, White_rook2Pos, White_horse1Pos, White_horse2Pos,  White_bishop1Pos, White_bishop2Pos, 
    White_queenPos, White_kingPos, White_pawn1Pos, White_pawn2Pos, White_pawn3Pos, White_pawn4Pos, White_pawn5Pos, White_pawn6Pos, White_pawn7Pos, White_pawn8Pos]
    return piecelist 


def black_pieces(screen):
    n=43.5
    

    #black rook 1
    Black_rook1 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Svart_tårn.png")
    Black_rook1 = pygame.transform.scale(Black_rook1, (n, n))
    Black_rook1Pos= screen.blit(Black_rook1, Bliste[0])

    #black rook 2
    Black_rook2 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Svart_tårn.png")
    Black_rook2 = pygame.transform.scale(Black_rook2, (n, n))
    Black_rook2Pos= screen.blit(Black_rook2, Bliste[1])

    #black horse 1
    Black_horse1 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Svart_hest.png")
    Black_horse1 = pygame.transform.scale(Black_horse1, (n, n))
    Black_horse1Pos= screen.blit(Black_horse1, Bliste[2])

    #black horse 2
    Black_horse2 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Svart_hest.png")
    Black_horse2 = pygame.transform.scale(Black_horse2, (n, n))
    Black_horse2Pos= screen.blit(Black_horse2, Bliste[3])

    #black bishop 1
    Black_bishop1 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Svart_biskop.png")
    Black_bishop1 = pygame.transform.scale(Black_bishop1, (n, n))
    Black_bishop1Pos= screen.blit(Black_bishop1, Bliste[4])

    #black bishop 2
    Black_bishop2 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Svart_biskop.png")
    Black_bishop2 = pygame.transform.scale(Black_bishop2, (n, n))
    Black_bishop2Pos= screen.blit(Black_bishop2, Bliste[5])

    #black queen
    Black_queen = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Svart_dronning.png")
    Black_queen = pygame.transform.scale(Black_queen, (n, n))
    Black_queenPos= screen.blit(Black_queen, Bliste[6])

    #black king
    Black_king = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Svart_konge.png")
    Black_king = pygame.transform.scale(Black_king, (n, n))
    Black_kingPos= screen.blit(Black_king, Bliste[7])

    #black pawn 1
    Black_pawn1 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Svart_bonde.png")
    Black_pawn1 = pygame.transform.scale(Black_pawn1, (n, n))
    Black_pawn1Pos= screen.blit(Black_pawn1, Bliste[8])

    #black pawn 2
    Black_pawn2 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Svart_bonde.png")
    Black_pawn2 = pygame.transform.scale(Black_pawn2, (n, n))
    Black_pawn2Pos= screen.blit(Black_pawn1, Bliste[9])

    #black pawn 3
    Black_pawn3 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Svart_bonde.png")
    Black_pawn3 = pygame.transform.scale(Black_pawn1, (n, n))
    Black_pawn3Pos= screen.blit(Black_pawn3, Bliste[10])

    #black pawn 4
    Black_pawn4 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Svart_bonde.png")
    Black_pawn4 = pygame.transform.scale(Black_pawn1, (n, n))
    Black_pawn4Pos= screen.blit(Black_pawn4, Bliste[11])

    #black pawn 5
    Black_pawn5 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Svart_bonde.png")
    Black_pawn5 = pygame.transform.scale(Black_pawn1, (n, n))
    Black_pawn5Pos= screen.blit(Black_pawn5, Bliste[12])

    #black pawn 6
    Black_pawn6 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Svart_bonde.png")
    Black_pawn6 = pygame.transform.scale(Black_pawn1, (n, n))
    Black_pawn6Pos= screen.blit(Black_pawn6, Bliste[13])

    #black pawn 7
    Black_pawn7 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Svart_bonde.png")
    Black_pawn7 = pygame.transform.scale(Black_pawn7, (n, n))
    Black_pawn7Pos= screen.blit(Black_pawn7, Bliste[14])

    #black pawn 8
    Black_pawn8 = pygame.image.load(r"C:\Users\henri\Desktop\Chess.exe\Pieces\Svart_bonde.png")
    Black_pawn8 = pygame.transform.scale(Black_pawn8, (n, n))
    Black_pawn8Pos= screen.blit(Black_pawn8, Bliste[15])

    piecelist = [Black_rook1Pos, Black_rook2Pos, Black_horse1Pos,  Black_horse2Pos, Black_bishop1Pos, Black_bishop2Pos, Black_queenPos, Black_kingPos, 
    Black_pawn1Pos, Black_pawn2Pos, Black_pawn3Pos, Black_pawn4Pos, Black_pawn5Pos, Black_pawn6Pos, Black_pawn7Pos, Black_pawn8Pos]
    return piecelist 

#Finner ut hvilken hvit brikke som ble trykt på, og hvor den ble trykt til
def HRepos(indeks, turn):
    a=True
    while a:
        for something in pygame.event.get():
            if something.type == pygame.QUIT:
                running = False
                return running
            elif something.type == pygame.MOUSEBUTTONDOWN:
                papa = something.pos
                for x in Chessboard(screen):
                    if x.collidepoint(papa):
                        for i in white_pieces(screen):
                            if i.collidepoint(papa):
                                return turn
                        Hvitliste[indeks]= x
                        for y in black_pieces(screen):
                            if y.collidepoint(papa):
                                yndex= black_pieces(screen).index(y)
                                Bliste[yndex]= (600,0)
                        Chessboard(screen)
                        white_pieces(screen)
                        black_pieces(screen)
                        pygame.display.flip()
                        turn = 2
                        return turn

#Finner ut hvilken svart brikke som ble trykt på, og hvor den ble trykt til            
def BRepos(indeks, turn):
    a=True
    while a:
        for something in pygame.event.get():
            if something.type == pygame.QUIT:
                running = False
                return running
            elif something.type == pygame.MOUSEBUTTONDOWN:
                papa = something.pos
                for x in Chessboard(screen):
                    if x.collidepoint(papa):
                        for i in black_pieces(screen):
                            if i.collidepoint(papa):
                                return turn
                        Bliste[indeks]= x
                        for y in white_pieces(screen):
                            if y.collidepoint(papa):
                                yndex= white_pieces(screen).index(y)
                                Hvitliste[yndex]= (600,0)     
                        Chessboard(screen)
                        black_pieces(screen)
                        white_pieces(screen)
                        pygame.display.flip()
                        turn= 1
                        return turn
             

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

        elif event.type == pygame.MOUSEBUTTONDOWN:
            Lastclick = event.pos
            if turn ==1:
                for i in white_pieces(screen):
                    if i.collidepoint(Lastclick):
                        indeks = white_pieces(screen).index(i)
                        turn = HRepos(indeks, turn)
                        
            if turn ==2:
                for i in black_pieces(screen):
                    if i.collidepoint(Lastclick):
                        indeks = black_pieces(screen).index(i)
                        turn = BRepos(indeks, turn)
                        
    
            
           
        


pygame.quit()