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
    def hillclimb(self, t_start):
        print "Running Hillclimb...\n"
        # initial conditions
        t_stop = t_start + 10
        list_endboards = []
        list_moves = []
        solution_found = False
        nodes_expanded = 1
        list_moves.append(copy.deepcopy(self))
        # run hillclimb with restarts for 10 seconds (if no solution found yet)
        while time.time() < t_stop and solution_found == False:
            # climb initial conditions
            climb = True
            cost = 0
            my_nodes_expanded = 1
            # keep climbing until local optimal reached
            while climb:
                self.checkTotalHittingQueens()
                current_h = self.h
                # print "CURRENT H: ", self.h
                # break if solution found
                if current_h == 0:
                    # print "SOLUTION FOUND!"
                    nodes_expanded -= 1
                    my_nodes_expanded -= 1
                    break
                # calculate h for all
                self.setAllBoardNodesHeuristic()
                # self.printBoard()
                # find lowest board
                lowest = self.findlowestH()
                if current_h > lowest[0]:
                    # move queen
                    for j in xrange(self.dimensions):
                        if (self.grid[lowest[1]][j].queen == True):
                            self.grid[lowest[1]][j].queen = False
                    # print "MOVING QUEEN TO " , lowest[1] , "," ,lowest[2]
                    self.grid[lowest[1]][lowest[2]].queen = True
                    nodes_expanded += 1
                    my_nodes_expanded += 1
                    cost += lowest[3]
                    list_moves.append(copy.deepcopy(self))
                else:
                    climb = False
            # check if local or global solution
            if current_h > 0:
                # print("LOCAL SOLUTION FOUND\n")
                list_moves = []
                result = [current_h, cost, nodes_expanded, solution_found, my_nodes_expanded]
                list_endboards.append(result)
                # reset board
                self.setNewRandomQueens()
                list_moves.append(copy.deepcopy(self))
            else:
                solution_found = True
                # print("GLOBAL SOLUTION FOUND\n")
                # self.printBoard()
                result = [current_h, cost, nodes_expanded, solution_found, list_moves, my_nodes_expanded]
                list_endboards.append(result)

        t_elapsed = time.time() - t_start
        # choose best solution out of restarts
        if len(list_endboards) > 0:
            best_result = list_endboards[0]
            for result in list_endboards:
                if result[0] < best_result[0]:
                    best_result = result
                elif result[0] == best_result[0]:
                    if result[1] < best_result[1]:
                        best_result = result
            # output data
            print "---HILLCLIMBING RESULTS---"
            print "Solved: ", solution_found
            print "Elapsed Time: ", t_elapsed, "seconds"
            print "# Nodes Expanded (total) = ", best_result[2]
            print "Cost (for best path) = ", best_result[1]
            if (solution_found):
                bfactor = str(best_result[2]) + "/" + str(best_result[5])
                print "Effective Branching factor: ", bfactor
                print "Path to Solution: \n"
                self.printHillMoves(best_result[4])
        # print moves
        # print "best result: ", best_result
        # print list_endboards

    # finds move with lowest heuristic value given board with h calculated
    def findlowestH(self):
        # go through each node and find lowest value
        lowest_h = self.h
        cost = 0
        low_i = 0
        low_j = 0
        # print "LOWEST H" , lowest_h
        # print "Finding lowest H on board"
        for i in xrange(self.dimensions):
            for j in xrange(self.dimensions):
                if (self.grid[i][j].queen != True):
                    # compare h value
                    if self.grid[i][j].h < lowest_h:
                        lowest_h = self.grid[i][j].h
                        low_i = i
                        low_j = j
                        cost = self.grid[i][j].g
                        # print"lowest H of ",lowest_h," found at [",i,"]","[",j,"]"
                    if self.grid[i][j].h == lowest_h:
                        # print "equal lowest H of ",lowest_h," found at [",i,"]","[",j,"]"
                        pass  # just keep first one

        return (lowest_h, low_i, low_j, cost)

    def printHillMoves(self, moves):
        for z, move in enumerate(moves):
            move.checkTotalHittingQueens()
            h = move.h
            # Clear values
            for i in xrange(self.dimensions):
                for j in xrange(self.dimensions):
                    if (move.grid[i][j].queen == False):
                        move.grid[i][j].h = 0
            # print board
            print "Move ", z, "--- H = ", h
            move.printBoard()


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
        # set heuristic back to this board
        self.checkTotalHittingQueens()

    #Runs A* with Iterative Deepining on initialized board to get the optimal solution (for 10 seconds)
    def aStarPQWithIterativeDeepining(self, startTime, bound):
        print("Running A* with iterative deepining")
        #Keep track of the expanded nodes (including the starting node)
        expandedNodes = 0
        #Keep track of successors
        branchingNodes = 0

        #Copying the board
        startBoard = copy.deepcopy(self)

        #Set the data of the board
        startBoard.checkTotalHittingQueens()

        #Keep track of the best board heuristic
        bestBoardH = startBoard.h
        bestBoardF = startBoard.f
        bestBoard = copy.deepcopy(startBoard)

        #Add the starting node to the priority queue
        openPQ =  PriorityQueue()
        openPQ.push(startBoard, startBoard.h)

        #Boards after evaluation
        closedSet = []

        #TimeLimit
        timeLimit = 10

        #Out time limit
        maxTime = startTime + timeLimit


        #Loop until the PQ is empty or until we find the solution
        while(openPQ.index >= 1 and (time.time()  < maxTime ) ):
            #The Current Board to be checked
            currentBoard = openPQ.pop()

            #Check if we have found a board that has no attacking queens
            if(currentBoard.h == 0):
                total_time =time.time()-startTime
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

                return (movesPath, expandedNodes, branchingNodes/expandedNodes, total_time, False)

            #Break if we have reached our time limit
            if(time.time() > maxTime):
                break

            #If the board has already been evaluated then loop from the beginning
            isInList = currentBoard.checkBoardInList(closedSet, startTime)

            if(isInList):
                continue

            #Since we are evaluting this node we want to add it in the closedSet
            closedSet.append(currentBoard)

            if(time.time() > maxTime):
                break

            #Create all the neighbor (possible moves) of that board
            currentBoard.neighbors = currentBoard.GetAllSuccessors(startTime)

            #Increase the expanded nodes
            expandedNodes += 1


            for curNeighbor in currentBoard.neighbors:
                branchingNodes += 1

                #Break if we have reached our time limit
                if(time.time()  > (startTime + timeLimit)):
                    break



                isInListTwo = curNeighbor.checkBoardInList(closedSet, startTime)


                if(not isInListTwo):
                    #Set the link
                    curNeighbor.previous = currentBoard
                    curNeighbor.h = curNeighbor.h * 30
                    #Add the neighbor in the Priority Q

                    #Only add it if it's less
                    if(currentBoard.f < bound):
                        openPQ.push(curNeighbor,curNeighbor.h + curNeighbor.g)


        #Total time elapsed
        total_time =time.time()-startTime

        #Print the best board if we ran out of time
        if (time.time()  > (startTime + timeLimit) ):
            print("The algorithm ran out of time " + str(total_time) + " and it did NOT found a solution")

            return None

        #If the while loop finishes without finding a solution
        #Then there is no solution for this problem (No attacking queens at all)
        print("No optimal solution is possible")
        return False

    #Runs A* on initialized board to get the optimal solution
    def aStarPQ(self, startTime):
        print("Running A*")
        #Keep track of the expanded nodes (including the starting node)
        expandedNodes = 0
        #Keep track of successors
        branchingNodes = 0

        #Copying the board
        startBoard = copy.deepcopy(self)

        #Set the data of the board
        startBoard.checkTotalHittingQueens()

        #Add the starting node to the priority queue
        openPQ =  PriorityQueue()
        openPQ.push(startBoard, startBoard.h)

        #Boards after evaluation
        closedSet = []

        #Out time limit
        maxTime = startTime + 10


        #Loop until the PQ is empty or until we find the solution
        while(openPQ.index >= 1 and (time.time()  < maxTime ) ):
            #The Current Board to be checked
            currentBoard = openPQ.pop()

            #Check if we have found a board that has no attacking queens
            if(currentBoard.h == 0):
                total_time =time.time()-startTime
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

                return (movesPath, expandedNodes, branchingNodes/expandedNodes, total_time)

            #Break if we have reached our time limit
            if(time.time() > maxTime):
                break

            #If the board has already been evaluated then loop from the beginning
            isInList = currentBoard.checkBoardInList(closedSet, startTime)

            if(isInList):
                continue

            #Since we are evaluting this node we want to add it in the closedSet
            closedSet.append(currentBoard)

            if(time.time() > maxTime):
                break

            #Create all the neighbor (possible moves) of that board
            currentBoard.neighbors = currentBoard.GetAllSuccessors(startTime)

            #Increase the expanded nodes
            expandedNodes += 1


            for curNeighbor in currentBoard.neighbors:
                branchingNodes += 1

                #Break if we have reached our time limit
                if(time.time()  > (startTime + 10)):
                    break

                isInListTwo = curNeighbor.checkBoardInList(closedSet, startTime)


                if(not isInListTwo):
                    #Set the link
                    curNeighbor.previous = currentBoard
                    curNeighbor.h = curNeighbor.h * 30
                    #Add the neighbor in the Priority Q
                    openPQ.push(curNeighbor,curNeighbor.h + curNeighbor.g)


        #Total time elapsed
        total_time =time.time()-startTime

        #Print the best board if we ran out of time
        if (time.time()  > (startTime + 10) ):
            print("The algorithm ran out of time " + str(total_time) + " and it did NOT found a solution")

            return None



        #If the while loop finishes without finding a solution
        #Then there is no solution for this problem (No attacking queens at all)
        print("No optimal solution is possible")
        return None

    #Checks if a board is already in a list by checking its queenPositions
    def checkBoardInList(self, list, startTime):

        for curBoard in list:
            #Break if we have reached our time limit
            if(time.time() > startTime + 10):
                return False

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
    def GetAllSuccessors(self,startTime):
        #Stores a list of all the possible moves
        AllpossibleBoards = []

        #Loop through the entire Board
        for i in xrange(self.dimensions):
            for j in xrange(self.dimensions):

                if(time.time() > startTime + 10):
                    break

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
            self.h = 10 + (totalAttacks/2)
            #self.h = totalAttacks/2



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
