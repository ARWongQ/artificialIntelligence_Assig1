import math
import random
from node import Node
import time

#The class for the Board
class Board:
    def __init__(self,n):
        self.dimensions = n
        self.h = 0
        self.grid = [[Node() for j in range(0,n)] for i in range(0,n) ]
        self.previous = None

    # performs hillclimbing algorithm on initialized board
    def hillclimb(self):
        print "RUNNING HILLCLIMB"
        # initial conditions
        t_stop = time.time() + 10
        list_endboards = []
        solution_found = False
        # run hillclimb with restarts for 10 seconds (if no solution found yet)
        # while time.time() < t_stop and not (solution_found):
        # climb initial conditions
        climb = True
        nodes_expanded = 1
        # keep climbing until local optimal reached
        while climb:
            self.checkTotalHittingQueens()
            current_h = self.h
            print "CURRENT H: ", self.h
            # break if solution found
            if current_h == 0:
                print "SOLUTION FOUND!"
                break
            # calculate h for all
            self.setAllBoardNodesHeuristic()
            self.printBoard()
            # find lowest board
            lowest = self.findlowestH()
            if current_h > lowest[0]:
                # move queen
                for j in xrange(self.dimensions):
                    if (self.grid[lowest[1]][j].queen == True):
                        self.grid[lowest[1]][j].queen = False
                self.grid[lowest[1]][lowest[2]].queen = True
                nodes_expanded += 1
            else:
                climb = False
        # check if local or global solution
        if current_h > 0:
            print("LOCAL SOLUTION FOUND\n")
            list_endboards.append(0)
        else:
            solution_found = True
            print("GLOBAL SOLUTION FOUND\n")
            list_endboards.append(0)
        # reset board
        # self.setNewRandomQueens()
        print "# nodes expanded = ", nodes_expanded
    # choose best solution out of restarts
    # output data

    # finds move with lowest heuristic value given board with h calculated
    def findlowestH(self):
        # go through each node and find lowest value
        lowest_h = self.h
        low_i = 0
        low_j = 0
        print "Finding lowest H on board"
        for i in xrange(self.dimensions):
            for j in xrange(self.dimensions):
                if (self.grid[i][j].queen != True):
                    # compare h value
                    if self.grid[i][j].h < lowest_h:
                        lowest_h = self.grid[i][j].h
                        low_i = i
                        low_j = j
                        print"lowest H of ",lowest_h," found at [",i,"]","[",j,"]"
                    if self.grid[i][j].h == lowest_h:
                        # come up with random choice
                        print "equal lowest H of ",lowest_h," found at [",i,"]","[",j,"]"
                        pass
        """
        # CLIMB ONCE
        self.checkTotalHittingQueens()
        current_h = self.h
        if current_h > lowest_h:
            # move queen
            for j in xrange(self.dimensions):
                if (self.grid[low_i][j].queen == True):
                    self.grid[low_i][j].queen = False
            self.grid[low_i][low_j].queen = True
            self.checkTotalHittingQueens()
        """

        return (lowest_h, low_i, low_j)


    #Sets the values of all the nodes in the Board to the lowest heuristic (#HittingQueens + #Tiles^2)
    def setAllBoardNodesHeuristic(self):
        print("Setting all the boards")

        #Loop through the entire Board
        for i in xrange(self.dimensions):
            for j in xrange(self.dimensions):
                if(self.grid[i][j].queen == True):
                    print("Checking Queen in Pos " + str(i) + " " + str(j))
                    self.getQueensMovesHeuristics(i,j)

    #Sets the heuristic for the given Queen's Row (Is)
    def getQueensMovesHeuristics(self,iQ,jQ):
        #Set the current position to not have a queen bc it will move
        self.grid[iQ][jQ].queen = False

        #Loop through the entire Row
        for j in xrange(self.dimensions):
            if(jQ != j):
                print("Checking Positions " + str(iQ) + " " + str(j))
                #set the position to be a queen
                self.grid[iQ][j].queen = True

                #Calculate and set the board's heuristic
                self.checkTotalHittingQueens()


                #Set The heuristic to the node
                movementCost = 10 + (abs(jQ - j) ** 2)

                nodeHeur = self.h

                print("These many queens are hitting each other " + str(nodeHeur))

                self.grid[iQ][j].h = nodeHeur
                self.grid[iQ][j].g = movementCost
                self.grid[iQ][j].f = nodeHeur + movementCost

                #Set the position to not longer be a queen
                self.grid[iQ][j].queen = False


        #Set the queen Back Position to have a queen
        self.grid[iQ][jQ].queen = True

    #Sums all the queens that are attacking
    def addTotalHittingQueens(self):
        totalAttacks = 0
        #Loop through the entire board and add the hitting queens
        for i in xrange(self.dimensions):
                for j in xrange(self.dimensions):
                    if(self.grid[i][j].queen == True):
                        totalAttacks += self.grid[i][j].hitting

        return totalAttacks

    #Clears all the hitting values of the nodes
    def clearAllNodeValues(self):
        #Loop through the entire board and set all the hitting to 0
        for i in xrange(self.dimensions):
                for j in xrange(self.dimensions):
                    self.grid[i][j].hitting = 0

    #Calculates the hitting Queens of the board and sets it to the heuristic
    def checkTotalHittingQueens(self):
        print("Checking how many queens are hitting each other")

        #Clear all the values to not double count
        self.clearAllNodeValues()

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
