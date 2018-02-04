
import random
from node import Node

#The class for the Board
class Board:
    def __init__(self,n):
        self.dimensions = n
        self.h = 0
        self.grid = [[Node() for j in range(0,n)] for i in range(0,n) ]
        self.previous = None


    #Calculates the hitting Queens of the board

    #Sets random Queens
    def setRandomQueens(self):
        print ("Setting random queens")

        queensToAdd = self.dimensions

        bound = self.dimensions - 1

        #Add n random queens
        while(queensToAdd > 0):
            i = random.randint(0,bound)
            j = random.randint(0,bound)

            if(self.grid[i][j].queen == False):
                self.grid[i][j].queen = True
                queensToAdd -= 1





    #Prints the Board to the user
    def printBoard(self):
        print ("Printing Board")

        #Prints all the elements inside the board
        for i in xrange(self.dimensions):
                for j in xrange(self.dimensions):

                    if(self.grid[i][j].queen != True):
                        print self.grid[i][j].h,
                    else:
                        print "Q",

                print("\n")
