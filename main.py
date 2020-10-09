import pygame
pygame.init()

win = pygame.display.set_mode((500,480))

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
    
    def draw(self, win):

class cellboard(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.status = 0 # kosong
        self.camp = 0 # bukan camp

    def setStatus(self,status):
        self.status = status # 0 = kosong; 1 = ada isi
    
    def draw(self, win):

class papan(object):
    def __init__(self,x,y):
        self.isi = []
        for i in range(x):
            for j in range(y):
                self.isi.append(cellboard(i,j))

    def draw(self, win):

# MODEL
class pemain(object):
    def __init__(self, player1):
        self.identity = player1 # red = 0, green = 1
        self.bidak = []
        for i in range()

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


# MAIN