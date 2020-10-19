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

class bisaLoncat:
    def __init__(self):
        self.bisa = False
        self.kemana = cellboard(8,8)



def bisaLompat(x,y,a,b):
    bisaLongcat = bisaLoncat()
    if (cekTetangga(x,y,a,b) and (board.isi[a][b].owner != board.isi[x][y].owner)):
        bisaLongcat.bisa = True
        bisaLongcat.kemana = board.isi[2*a-x][2*b - y]
    return bisaLongcat

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
