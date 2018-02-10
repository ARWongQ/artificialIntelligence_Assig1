import math
import random
from node import Node
from queenPos import QueenPos
from priorityQueue import PriorityQueue
import time
import copy

#The class for the Board
class Board:
    def __init__(self,n):
        self.dimensions = n
        self.h = 0
        self.g = 0
        self.f = 0
        self.grid = [[Node() for j in range(0,n)] for i in range(0,n) ]
        self.neighbors = []
        self.previous = None
        self.queenPositions = []


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

            self.printBoard()
        else:
            solution_found = True
            print("GLOBAL SOLUTION FOUND\n")
            list_endboards.append(0)

            self.printBoard()

        # reset board
        # self.setNewRandomQueens()
        print "# nodes expanded = ", nodes_expanded
    # choose best solution out of restarts
    # output data

    # finds move with lowest heuristic value given board with h calculated
    def findlowestH(self):
        # go through each node and find lowest value
        lowest_h = self.h #Why is this lowest_h ? when you wnat the lowest node
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

        #Loop through the entire Board
        for i in xrange(self.dimensions):
            for j in xrange(self.dimensions):
                if(self.grid[i][j].queen == True):
                    self.getQueensMovesHeuristics(i,j)

    #Sets the heuristic for the given Queen's Row (Is)
    def getQueensMovesHeuristics(self,iQ,jQ):
        #Set the current position to not have a queen bc it will move
        self.grid[iQ][jQ].queen = False

        #Loop through the entire Row
        for j in xrange(self.dimensions):
            if(jQ != j):
                #set the position to be a queen
                self.grid[iQ][j].queen = True

                #Calculate and set the board's heuristic
                self.checkTotalHittingQueens()


                #Set The heuristic to the node
                movementCost = 10 + (abs(jQ - j) ** 2)

                nodeHeur = self.h

                self.grid[iQ][j].h = nodeHeur
                self.grid[iQ][j].g = movementCost
                self.grid[iQ][j].f = nodeHeur + movementCost

                #Set the position to not longer be a queen
                self.grid[iQ][j].queen = False


        #Set the queen Back Position to have a queen
        self.grid[iQ][jQ].queen = True



    #Runs A* on initialized board to get the optimal solution
    def aStarPQ(self):
        print("Running A*")

        #Copying the board
        startBoard = copy.deepcopy(self)

        #Set the data of the board
        startBoard.checkTotalHittingQueens()

        #Add the starting node to the priority queue
        openPQ =  PriorityQueue()
        openPQ.push(startBoard, startBoard.h)

        #Boards after evaluation
        closedSet = []

        #Loop until the PQ is empty or until we find the solution
        while(openPQ.index >= 1):
            #The Current Board to be checked
            currentBoard = openPQ.pop()

            #Check if we have found a board that has no attacking queens
            if(currentBoard.h == 0):
                #Success
                print("We have found a solution")

                #Make the path towards the solution
                movesPath = []
                temp = currentBoard
                movesPath.append(temp)

                #Add the order of the path (backtracking)
                while(temp.previous):
                    movesPath.append(temp.previous)
                    temp = temp.previous

                return movesPath



            #print("Evaluating Board")
            #If the board has already been evaluated then loop from the beginning
            isInList = currentBoard.checkBoardInList(closedSet)
            #print("Hello World1")
            if(isInList):
                continue



            #Since we are evaluting this node we want to add it in the closedSet
            closedSet.append(currentBoard)

            #Create all the neighbor (possible moves) of that board
            currentBoard.neighbors = currentBoard.GetAllSuccessors()

            for curNeighbor in currentBoard.neighbors:
                #print("Checking Neighbor")
                #Check if the node has not already been evaluated
                isInListTwo = curNeighbor.checkBoardInList(closedSet)

                if(not isInListTwo):
                    #Set the link
                    curNeighbor.previous = currentBoard
                    curNeighbor.h = curNeighbor.h * 20
                    #Add the neighbor in the Priority Q
                    openPQ.push(curNeighbor,curNeighbor.h + curNeighbor.g)

        #If the while loop finishes without finding a solution
        #Then there is no solution for this problem (No attacking queens at all)
        print("No optimal solution is possible")
        return

    #Checks if a board is already in a list by checking its queenPositions
    def checkBoardInList(self, list):

        for curBoard in list:

            sameBoard =self.checkBoardWithBoard(curBoard)

            if(sameBoard == True):
                return True

        return False

    def checkBoardWithBoard(self, BoardToCompare):
        boardQueensPos = self.queenPositions

        i = 0
        for queenListPos in BoardToCompare.queenPositions:

                currI = boardQueensPos[i].i
                checkingI = queenListPos.i

                currJ = boardQueensPos[i].j
                checkingJ = queenListPos.j
                i+=1

                if(currI != checkingI or currJ != checkingJ):
                    return False

        return True






    #Gets all the successors (possible moves) from a give board
    def GetAllSuccessors(self):
        #Stores a list of all the possible moves
        AllpossibleBoards = []

        #Loop through the entire Board
        for i in xrange(self.dimensions):
            for j in xrange(self.dimensions):
                if(self.grid[i][j].queen == True):
                    #Get n-1 boards for that row
                    currentPossible = self.getQueenSuccesor(i,j)

                    #Append the row
                    for k in xrange(self.dimensions - 1):
                        AllpossibleBoards.append(currentPossible[k])

        return AllpossibleBoards


    #Return a list n-1 of boards (possible moves)
    def getQueenSuccesor(self,iQ,jQ):
        #Store the possible list for this outcome
        possibleBoards = []

        #Set the current position to not have a queen bc it will move
        self.grid[iQ][jQ].queen = False

        #Loop through the entire Row
        for j in xrange(self.dimensions):

            if(jQ != j):
                #set the position to be a queen
                self.grid[iQ][j].queen = True

                #Calculate and set the board's heuristic
                self.checkTotalHittingQueens()


                #Set The heuristic to the node
                movementCost = 10 + (abs(jQ - j) ** 2)

                tempG = self.g + movementCost


                #Make a deep copy of the object
                tempBoard = copy.deepcopy(self)
                tempBoard.g = tempG
                tempBoard.f = tempBoard.g + tempBoard.h
                #Add the new Queen Position
                tempBoard.queenPositions[iQ] = QueenPos(iQ,j)

                #Append to the possibleBoards
                possibleBoards.append(tempBoard)

                #Set the position to not longer be a queen
                self.grid[iQ][j].queen = False


        #Set the queen Back Position to have a queen
        self.grid[iQ][jQ].queen = True

        #Return the list of possible boards
        return possibleBoards




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
        #print("Checking how many queens are hitting each other")

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


    def setRandomQueensTwo(self):
        #print("Setting random queens")
        #Range of random integer
        bound = self.dimensions - 1

        for i in xrange(self.dimensions):
            j = random.randint(0,bound)
            self.grid[i][j].queen = True
            self.queenPositions.append(QueenPos(i,j))




    #Sets random Queens
    def setRandomQueens(self):
        #print ("Setting random queens")

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
