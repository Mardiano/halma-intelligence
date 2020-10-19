import random
from papan import cellboard, papan, startstate

# arr = [1,4,2,4,1,41,151,0,14]
#
# print(random.choice(arr))

#TREE
class Tree:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []

    def addChild(self, child):
        self.children.append(child)

    def getChild(self, i):
        return self.children[i]

    def getRandomSuccessor(self):
        return random.choice(self.children)

#HILL CLIMBING
def hillClimbing(root):
    current = root
    while True:
        neighbor = current.getRandomSuccessor()
        if neighbor.data < current.data:
            return current.data
        current = neighbor

#DUMMY ROOT
def makeInitialBoard(n):
    matriks = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if (i+j <= (n/2 -1)) or (3*n/2-1 <= i+j <= 2*(n-1)):
                matriks[i][j] = 1

    return matriks


# board = papan(8,8)
#
# print(sumScore(board, 0))
