
import random
from node import Node

#The class for the Board
class Board:
    def __init__(self,n):
        self.dimensions = n
        self.h = 0
        self.grid = [[Node() for j in range(0,n)] for i in range(0,n) ]
        self.previous = None


    #Sums all the queens that are attacking
    def addTotalHittingQueens(self):
        totalAttacks = 0
        for i in xrange(self.dimensions):
                for j in xrange(self.dimensions):
                    if(self.grid[i][j].queen == True):
                        totalAttacks += self.grid[i][j].hitting

        return totalAttacks

    #Calculates the hitting Queens of the board and sets it to the heuristic
    def checkTotalHittingQueens(self):
        print("Checking how many queens are hitting each other")

        #Loop through all the nodes in the board
        for i in xrange(self.dimensions):
                for j in xrange(self.dimensions):
                    if(self.grid[i][j].queen == True):
                        #If its a queen then check which queens its hitting
                        self.checkHittingQueens(i,j)

        #Sum up all the .hitting that each queen is hitting
        totalAttacks = self.addTotalHittingQueens()

        #Set the heurstic
        if(totalAttacks == 0):
            self.h = 0
        else:
            #self.h = 10 + totalAttacks/2
            self.h = totalAttacks/2



    #Checks how many queens is hitting Horizontally
    def checkHorizontalAttacks(self,i,j):
        for j_t in xrange(self.dimensions):
            if(self.grid[i][j_t].queen == True and j_t != j):
                self.grid[i][j].hitting += 1


    #Checks how many queens is hitting Vertically
    def checkVerticalAttacks(self,i,j):
        for i_t in xrange(self.dimensions):
            if(self.grid[i_t][j].queen == True and i_t != i):
                self.grid[i][j].hitting += 1

    #Checks ho wmany queens is hitting Diagonally /
    def checkDiagonalFAttacks(self,i,j):
        currI = i
        currJ = j

        #Go to the bottom
        while(currI != 0 and currJ != (self.dimensions-1)):
            currI -= 1
            currJ += 1

        #Check diagonally
        for i_t in xrange(self.dimensions):
            newI = currI+i_t
            newJ = currJ-i_t
            if(newI < self.dimensions and newJ >= 0):
                if(self.grid[newI][newJ].queen == True and (newI != i and newJ != j)):
                    self.grid[i][j].hitting += 1


    #Diagonal \
    def checkDiagonalBAttacks(self,i,j):
        currI = i
        currJ = j
        #Go to the top
        while(currI != 0 and currJ != 0):
            currI -= 1
            currJ -= 1

        #Check diagonally
        for i_t in xrange(self.dimensions):
            newI = currI+i_t
            newJ = currJ+i_t
            if(newI < self.dimensions and newJ < self.dimensions):
                if(self.grid[newI][newJ].queen == True and (newI != i and newJ != j) ):
                    self.grid[i][j].hitting += 1


    #Check how many queens this queen is hitting
    def checkHittingQueens(self,i,j):
        self.checkHorizontalAttacks(i,j)
        self.checkVerticalAttacks(i,j)
        self.checkDiagonalBAttacks(i,j)
        self.checkDiagonalFAttacks(i,j)

    #Clears the Queens in a board
    def clearQueens(self):
         for i in xrange(self.dimensions):
                for j in xrange(self.dimensions):
                    self.grid[i][j].queen = False


    #Set new Random Queens
    def setNewRandomQueens(self):

        #Clears remaining Queens
        self.clearQueens()
        #Sets new Queens
        self.setRandomQueens()

    #Sets random Queens
    def setRandomQueens(self):
        print ("Setting random queens")

        queensToAdd = self.dimensions
        bound = self.dimensions - 1

        #List of Booleans to keep track of the taken rows (Is)
        takenIs = [False for i in range(queensToAdd)]

        #Add n random queens
        while(queensToAdd > 0):
            #Get random Is and Js
            i = random.randint(0,bound)
            j = random.randint(0,bound)

            #Check if the spot is taken
            if(self.grid[i][j].queen == False):
                #Check if the row is not taken
                if(takenIs[i] == False):
                    #Add the queen and check the spot as taken
                    self.grid[i][j].queen = True
                    queensToAdd -= 1
                    takenIs[i] = True


    #Prints the Board to the user
    def printBoard(self):
        print ("Printing Board")

        #Prints all the elements inside the board
        for i in xrange(self.dimensions):
                for j in xrange(self.dimensions):

                    #Check if the node is not a queen
                    if(self.grid[i][j].queen != True):
                        print self.grid[i][j].h,
                    else:
                        #Print Q because is a queen
                        print "Q",

                print("\n")
