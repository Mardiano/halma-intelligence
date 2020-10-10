import pygame
pygame.init()

win = pygame.display.set_mode((1280,720))

pygame.display.set_caption("Bacod Adit")
"""
# UTIL
class matriks():
    def __init__(self,lebar,tinggi):
        self.lebar = lebar
        self.tinggi = y
        self.rows = [[0]*lebar for i in range(tinggi)]
"""

# OBJECT
class bidak(object):
    def __init__(self,x,y,owner):
        self.x = x
        self.y = y
        self.owner = owner
    
    #def draw(self, win):

class cellboard(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.status = 0 # kosong
        self.camp = 0 # bukan camp

    def setStatus(self,status):
        self.status = status # 0 = kosong; 1 = ada isi
    
    def draw(self, win):
        bidak1 = pygame.image.load('cellboard.png')
        bidak1 = pygame.transform.scale(bidak1, (50, 50))
        panjang = 262
        lebar = 130
        colsize = 55
        rowsize = 58
        win.blit(bidak1, ((panjang + self.x * colsize), lebar + (self.y * rowsize)))

class papan(object):
    def __init__(self,x,y):
        self.isi = [[]*x for i in range(y)]
        self.x = x
        self.y = y
        i = 0
        j = 0
        for i in range(self.x):
            for j in range(self.y):
                self.isi[i].append(cellboard(i,j))

    def draw(self, win):
        #x = 262
        #y = 130
        #colsize = 55
        #rowsize = 58
        for i in range(self.x):
            for j in range(self.y):
                self.isi[i][j].draw(win)

class startstate(object):
    def __init__(self):
        self.row = 0
        self.color = 0

    def setrow(self,row):
        self.row = row

    def setcol(self,col):
        self.color = col 

    def draw(self,win):
        rad1but = pygame.image.load('radio-8.png')
        rad1but = pygame.transform.scale(rad1but, (60, 24))
        win.blit(rad1but, (500, 390))
        rad2but = pygame.image.load('radio-10.png')
        rad2but = pygame.transform.scale(rad2but, (60, 24))
        win.blit(rad2but, (600, 390))
        rad3but = pygame.image.load('radio-16.png')
        rad3but = pygame.transform.scale(rad3but, (60, 24))
        win.blit(rad3but, (710, 390))
        col1but = pygame.image.load('radio-red.png')
        col1but = pygame.transform.scale(col1but, (90, 24))
        win.blit(col1but, (680, 500))
        col2but = pygame.image.load('radio-yellow.png')
        col2but = pygame.transform.scale(col2but, (145, 24))
        win.blit(col2but, (475, 500))

# MODEL
class pemain(object):
    def __init__(self, player1):
        self.identity = player1 # red = 0, green = 1
        self.bidak = []
        #for i in range()

class gamestate(object):
    def __init__(self, turn, win):
        self.turn = turn
        self.win = win

    def changeTurn(self,turn):
        self.turn = turn

    def setWinner(self,win):
        self.win = win


def redrawGameWindow():
    win.blit(bg, (0,0))
    papan.draw(win)
    for bidak in pemain1.bidak:
        bidak.draw(win)
    for bidak in pemain2.bidak:
        bidak.draw(win)
    
    pygame.display.update()

def redrawGameWindow():
    win.blit(bg, (0,0))
    if start:
        halma.draw(win)
    if not start: 
        board.draw(win)
        okbut =  pygame.image.load('okbut.png')
        okbut = pygame.transform.scale(okbut, (241, 60))
        win.blit(okbut, (1020, 280))
        quitbut =  pygame.image.load('quitbut.png')
        quitbut = pygame.transform.scale(quitbut, (241, 60))
        win.blit(quitbut, (1020, 380))
        play1 =  pygame.image.load('player-one.png')
        play1 = pygame.transform.scale(play1, (126, 46))
        win.blit(play1, (842, 670))
        play2 =  pygame.image.load('player-two.png')
        play2 = pygame.transform.scale(play2, (126, 46))
        win.blit(play2, (10, 10))

    pygame.display.update()

# MAIN

halma = startstate()
board = papan(8,8)

run = True
start = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if start:
        bg = pygame.image.load('bgstart.png')
        bg = pygame.transform.scale(bg, (1280, 720))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            start = False
    else:
        bg = pygame.image.load('bggame.png')
        bg = pygame.transform.scale(bg, (1280, 720))

    redrawGameWindow()
    

pygame.quit()