import random

# arr = [1,4,2,4,1,41,151,0,14]
#
# print(random.choice(arr))


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

def hillClimbing(root):
    current = root
    while True:
        neighbor = current.getRandomSuccessor()
        if neighbor.data < current.data:
            return current.data
        current = neighbor

def makeInitialBoard(n):
    matriks = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if (i+j <= (n/2 -1)) or (3*n/2-1 <= i+j <= 2*(n-1)):
                matriks[i][j] = 1

    return matriks

# def sumScore(state):
#     n = state.x
#
#     sum= 0
#     for i in range(n):
#         for j in range(n):
#             if state.isi[i][j].status == 1:
#
#
#
#
#
#
#
#     return sum




def makeTree():
    init = makeInitialBoard(8)


a = makeInitialBoard(8)
print(a)
print(len(a))
print(sumScore(a))
