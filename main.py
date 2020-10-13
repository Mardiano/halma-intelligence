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
    bidak1 = [pygame.image.load('cellboard-kosong.png').convert(), pygame.image.load('cellboard-bidak1.png'), pygame.image.load('cellboard-bidak1-move.png'), pygame.image.load('cellboard-bidak2.png'), pygame.image.load('cellboard-bidak2-move.png')]
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.status = 0 # kosong
        self.camp = 0 # bukan camp
        self.clicked = 0
        self.isStart = 0
        self.owner = 2
        self.hitbox = ((262 + self.x * 55), (130 + self.y * 58), 53, 56)

    def setStatus(self,status):
        self.status = status # 0 = kosong; 1,2,3,4 = ada isi
    
    def draw(self, win):
        if (self.isStart == 0 or self.clicked == 1):
            bidak1 = pygame.transform.scale(self.bidak1[self.status], (50, 50))
            panjang = 262
            lebar = 130
            colsize = 55
            rowsize = 58
            win.blit(bidak1, ((panjang + self.x * colsize), lebar + (self.y * rowsize)))
            self.isStart = 0
            pygame.draw.rect(win, (255,0,0), self.hitbox,2)

class papan(object):
    okbut =  pygame.image.load('okbut.png')
    okbut = pygame.transform.scale(okbut, (241, 60))
    quitbut =  pygame.image.load('quitbut.png')
    quitbut = pygame.transform.scale(quitbut, (241, 60))
    play1 =  [pygame.image.load('player-one-turn.png'), pygame.image.load('player-one.png')]
    play2 =  [pygame.image.load('player-two.png'), pygame.image.load('player-two-turn.png')]
        

    def __init__(self,x,y):
        self.isi = [[]*x for i in range(y)]
        self.x = x
        self.y = y
        self.okayhitbox = (1020, 280, 241, 60)
        self.quithitbox = (1020, 380, 241, 60)
        self.turn = 0 # 0 player 1, 1 player 2
        #self.isStart = 1
        #self.turnChanged = 0
        i = 0
        j = 0
        for i in range(self.x):
            for j in range(self.y):
                self.isi[i].append(cellboard(i,j))
                if (i + j <= (x-5)):
                    self.isi[i][j].camp = 1
                    self.isi[i][j].status = 1
                    self.isi[i][j].owner = 0
                if ((((x-1)*2)-(i+j)) <= 3):
                    self.isi[i][j].camp = 2
                    self.isi[i][j].status = 3
                    self.isi[i][j].owner = 1
        

    def changeturn(self):
        if self.turn == 1:
            self.turn = 0
        else:
            self.turn = 1

    def draw(self, win):
        #x = 262
        #y = 130
        #colsize = 55
        #rowsize = 58
        for i in range(self.x):
                for j in range(self.y):
                    self.isi[i][j].draw(win)
            
        play1 = pygame.transform.scale(self.play1[self.turn], (126, 46))
        win.blit(play1, (842, 670))

        play2 = pygame.transform.scale(self.play2[self.turn], (126, 46))
        win.blit(play2, (10, 10))

        win.blit(self.okbut, (1020, 280))
        pygame.draw.rect(win, (255,0,0), self.okayhitbox,2)
        win.blit(self.quitbut, (1020, 380))
        pygame.draw.rect(win, (255,0,0), self.quithitbox,2)

class startstate(object):
    rad1but = [pygame.image.load('radio-8.png'), pygame.image.load('radio-8-clicked.png')]
    rad2but = [pygame.image.load('radio-10.png'), pygame.image.load('radio-10-clicked.png')]
    rad3but = [pygame.image.load('radio-16.png'), pygame.image.load('radio-16-clicked.png')]
    col1but = pygame.image.load('radio-red.png')
    col2but = pygame.image.load('radio-yellow.png')
    col2but = pygame.transform.scale(col2but, (145, 24))
    col1but = pygame.transform.scale(col1but, (90, 24))
    win.blit(col1but, (680, 500))      
    win.blit(col2but, (475, 500))

    def __init__(self):
        self.row = 0 # 0 Null, 4 8x8 row, 2 10x10 row, 3 16x16 row
        self.player1 = 0  #0 human, 1 AI-Minimax, 2 AI-Minimax + Local search -> color auto red
        self.player2 = 0  #0 human, 1 AI-Minimax, 2 AI-Minimax + Local search -> color auto yellow
        self.rad1hitbox = (490, 387, 65, 30)
        self.rad2hitbox = (590, 387, 75, 30)
        self.rad3hitbox = (700, 387, 75, 30)
        
    def setrow(self,row):
        self.row = row

    def setplayer1(self,player1):
        self.player1 = player1 
    
    def setplayer2(self,player2):
        self.player2 = player2

    def draw(self,win):
        rad1but = pygame.transform.scale(self.rad1but[ ((3-self.row) // 2) * self.row], (60, 24))
        win.blit(rad1but, (500, 390))
        pygame.draw.rect(win, (255,0,0), self.rad1hitbox,2)
        
        rad2but = pygame.transform.scale(self.rad2but[ (1 - (self.row % 2)) * (self.row // 2)], (60, 24))
        win.blit(rad2but, (600, 390))
        pygame.draw.rect(win, (255,0,0), self.rad2hitbox,2)
        
        rad3but = pygame.transform.scale(self.rad3but[self.row // 3], (60, 24))
        win.blit(rad3but, (710, 390))
        pygame.draw.rect(win, (255,0,0), self.rad3hitbox,2)

# MODEL
"""
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
"""

def redrawGameWindow():
    if start:
        halma.draw(win)
    if not start: 
        board.draw(win)
    pygame.display.update()

def liatSekitar(x,y,size):
    adaSomething = False
    if (x != 0 and x != size-1) and (y != 0 and y != size-1):
        adaSomething = (board.isi[x-1][y].status and board.isi[x-1][y+1].status and board.isi[x-1][y-1].status and board.isi[x+1][y].status and board.isi[x+1][y+1].status and board.isi[x+1][y-1].status and board.isi[x][y+1].status and board.isi[x][y-1].status)
    if (x == 0 and (y != 0 and y != size-1)):
        adaSomething = board.isi[x+1][y].status and board.isi[x+1][y+1].status and board.isi[x+1][y-1].status and board.isi[x][y+1].status and board.isi[x][y-1].status
    if (x == size-1 and (y != 0 and y != size-1)):
        adaSomething =  board.isi[x-1][y].status and board.isi[x-1][y+1].status and board.isi[x-1][y-1].status and board.isi[x][y+1].status and board.isi[x][y-1].status
    if (y == 0 and (x != 0 and x != size-1)):
        adaSomething =  board.isi[x-1][y].status and board.isi[x-1][y+1].status and board.isi[x+1][y].status and board.isi[x+1][y+1].status and board.isi[x][y+1].status
    if (y == size-1 and (x != 0 and x != size-1)):
        adaSomething =  board.isi[x-1][y].status and board.isi[x-1][y-1].status and board.isi[x+1][y].status and board.isi[x+1][y-1].status and board.isi[x][y-1].status
    if (x == 0 and y == 0):
        adaSomething = (board.isi[x+1][y].status and board.isi[x+1][y+1].status and board.isi[x][y+1].status)
    if (x == size-1 and y == size-1):
        adaSomething = (board.isi[x-1][y].status and board.isi[x-1][y-1].status and board.isi[x][y-1].status)
    if (x == 0 and y == size-1):
        adaSomething = (board.isi[x+1][y].status and board.isi[x+1][y-1].status and board.isi[x][y-1].status)
    if (x == size-1 and y == 0):
        adaSomething = (board.isi[x-1][y].status and board.isi[x-1][y+1].status and board.isi[x][y+1].status)
    return adaSomething

class bisaLoncat: 
    def __init__(self): 
        self.bisa = False
        self.kemana = cellboard(8,8)  

def cekTetangga(x,y,a,b): #tambahin buat cek tetangga karena ada bidak musuh ntar
    return (x-a == 1 and y-b == 1) or (a-x == 1 and y-b == 1) or (x-a == 1 and b-y == 1) or (a-x == 1 and b-y == 1) or (x-a == 0 and y-b == 1) or (x-a == 1 and y-b == 0) or (x-a == 0 and b-y == 1) or (a-x == 1 and y-b == 0)

def bisaLompat(x,y,a,b):
    bisaLongcat = bisaLoncat()
    if (cekTetangga(x,y,a,b) and (board.isi[a][b].owner != board.isi[x][y].owner)):
        bisaLongcat.bisa = True
        bisaLongcat.kemana = board.isi[2*a-x][2*b - y]
    return bisaLongcat

# MAIN

halma = startstate()
board = papan(8,8)

run = True
start = True
hasSetting = False
bg1 = [pygame.image.load('bgstart.png'), pygame.image.load('bggame.png')]
bg = pygame.transform.scale(bg1[0], (1280, 720))
win.blit(bg, (0,0))
curPiece = []
countLoop = 1
sedangLoncat = False

while run:
    if start:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
                x, y = event.pos
                #print(x,y)
                if (x >= halma.rad1hitbox[0] and x <= halma.rad1hitbox[0] + halma.rad1hitbox[2] and y >= halma.rad1hitbox[1] and y <= halma.rad1hitbox[1] + halma.rad1hitbox[3]):
                    halma.setrow(1)
                    hasSetting = True
                elif (x >= halma.rad2hitbox[0] and x <= halma.rad2hitbox[0] + halma.rad2hitbox[2] and y >= halma.rad2hitbox[1] and y <= halma.rad2hitbox[1] + halma.rad2hitbox[3]):
                    halma.setrow(2)
                    hasSetting = True
                elif (x >= halma.rad3hitbox[0] and x <= halma.rad3hitbox[0] + halma.rad3hitbox[2] and y >= halma.rad3hitbox[1] and y <= halma.rad3hitbox[1] + halma.rad3hitbox[3]):
                    halma.setrow(3)
                    hasSetting = True
            if hasSetting:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        start = False
                        bg = pygame.transform.scale(bg1[1], (1280, 720))
                        win.blit(bg, (0,0))
            if event.type == pygame.QUIT:
                run = False
    else:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect(board.quithitbox).collidepoint(event.pos):
                    print("Lagi diklik quitnya")
                    for kotak in curPiece:
                        kotak.clicked = 0
                        if kotak == firstPiece:
                            kotak.setStatus(kotak.status-1)
                        else:
                            kotak.setStatus(kotak.status-((firstPiece.owner+1)*2))
                    curPiece.clear()
                    lastX, lastY = -1, -1
                    countLoop = 1
                    sedangLoncat = False
                if pygame.Rect(board.okayhitbox).collidepoint(event.pos):
                    if (len(curPiece) > 1):
                        print("Lagi diklik okaynya")
                        board.changeturn()
                        for kotak in curPiece:
                            kotak.clicked = 0
                            if kotak == lastPiece:
                                kotak.setStatus(kotak.status - 1)
                            else:
                                kotak.setStatus(0)
                        curPiece.clear()
                        lastX, lastY = -1, -1
                        countLoop = 1
                        sedangLoncat = False
                    else:
                        board.changeturn()
                        for kotak in curPiece:
                            kotak.setStatus(kotak.status - 1)
                            kotak.clicked = 0
                        curPiece.clear()
                        lastX, lastY = -1, -1
                        countLoop = 1
                        sedangLoncat = False
                for i in range(8):
                    for j in range(8):
                        if pygame.Rect(board.isi[i][j].hitbox).collidepoint(event.pos):
                            if not curPiece:
                                if (board.isi[i][j].owner == board.turn) and ((board.isi[i][j].status == 1) or (board.isi[i][j].status == 3)):
                                    print("Lagi diklik kotaknya")
                                    board.isi[i][j].clicked = 1
                                    lastX, lastY = i, j
                                    board.isi[i][j].setStatus(board.isi[i][j].status+1)
                                    curPiece.append(board.isi[i][j])
                                    firstPiece = board.isi[i][j]
                                    print("udah diklik kotaknya")
                            else:
                                #print("Lagi diklik klik ya kotaknya ", i, j, board.isi[i][j].owner, board.turn)
                                if (firstPiece.owner == board.turn and countLoop > 0 and board.isi[i][j].status == 0):
                                    a = int((i + lastX)/2)
                                    b = int((j + lastY)/2)
                                    print(board.isi[a][b].status, board.isi[lastX][lastY].status )
                                    if not ((firstPiece.owner == 1 and firstPiece.camp == 1 and board.isi[i][j].camp != 1) or (firstPiece.owner == 0 and firstPiece.camp == 2 and board.isi[i][j].camp != 2)):
                                        if (cekTetangga(a,b,lastX,lastY) and (((board.isi[a][b].status == 1) and (board.isi[lastX][lastY].status == 4)) or ((board.isi[a][b].status == 3) and (board.isi[lastX][lastY].status == 2)))):
                                            board.isi[i][j].setStatus(board.isi[i][j].status+((firstPiece.owner+1)*2))
                                            curPiece.append(board.isi[i][j])
                                            lastX, lastY = i, j
                                            print("Lagi diklik kotaknya")
                                            board.isi[i][j].clicked = 1
                                            print(board.isi[i][j].status)
                                            board.isi[i][j].owner = firstPiece.owner
                                            lastPiece = board.isi[i][j]
                                            sedangLoncat = True
                                        if (sedangLoncat == False and cekTetangga(i,j,lastX,lastY)):
                                            countLoop -= 1
                                            board.isi[i][j].setStatus(board.isi[i][j].status+((firstPiece.owner+1)*2))
                                            curPiece.append(board.isi[i][j])
                                            lastX, lastY = i, j
                                            print("Lagi diklik kotaknya")
                                            board.isi[i][j].clicked = 1
                                            print(board.isi[i][j].status)
                                            board.isi[i][j].owner = firstPiece.owner
                                            lastPiece = board.isi[i][j]
                                    
                                        
                """                   
                if curPiece:
                    for kotak in curPiece:
                        kotak.clicked = 0
                        if kotak == firstPiece:
                            board.isi[i][j].setStatus(board.isi[i][j].status+1)
                        else:
                            board.isi[i][j].setStatus(board.isi[i][j].status-((board.isi[i][j].owner+1)*2))
                    curPiece.clear()
                    lastX, lastY = -1, -1
            """

            if event.type == pygame.QUIT:
                run = False
            
    redrawGameWindow()
    

pygame.quit()