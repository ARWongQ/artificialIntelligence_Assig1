#The class for the Board
class myBoard:
    def __init__(self,n,h):
        self.dimensions = n
        self.h = 0
        self.grid = [[0 for j in range(0,n)] for i in range(0,n) ]
        #self.gridOfNodes = [[Node(0,0,False,0) for j in range(0,n)] for i in range(0,n) ]
        #self.previous = None
