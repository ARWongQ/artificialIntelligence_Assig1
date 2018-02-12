import time
import copy
from Board import Board
from queenPos import QueenPos

#Prints the stats for A* given the data
def printStats(movesPath, expandedNodes, successors, totalTime, nValue, astar):
    #Keep track of the current board and the cost to reach it
    i = 0
    lastBoardCost = 0
    for currBoard in reversed(movesPath):

        #Don't print the first board
        if(i == 0):
            i += 1
            continue

        print("Step " + str(i) + " ----------")

        currBoard.printBoard()

        #Keep track of the total cost
        lastBoardCost = currBoard.g
        i += 1


    if (astar):
        print("It took A* "+ str(totalTime) + " seconds to solve the "+ str(nValue) +"-queens problem")
    else:
        print("It took A* (iterative deep) " + str(totalTime) + " seconds to solve the " + str(nValue) + "-queens problem")
    print("With Expanded Nodes: " + str(expandedNodes))
    print("With successor per node of " + str(successors))
    print("With an effective branching factor of "+ str(expandedNodes) + "/" + str(len(movesPath) - 1))
    print("And a cost of " + str(lastBoardCost))


#Main Function
def main():
    print("Running nQueens")

    # Start the time
    startTime = time.time()

    #Get the n Value and the type of Search for the problem
    nValue = input("N value for the N-queens problem: ")
    searchType = input("Types of Search \n 1 for A* and \n 2 for greedy hill climbing \n 3 for A* with iterative Deepining: ")

    #Start the Board
    gameBoard = Board(nValue)
    # Set Random Queens
    gameBoard.setRandomQueensTwo()
    print(" ")
    # Print the first boards
    print("The starting Board is ---------")
    gameBoard.printBoard()

    astar = False

    if searchType == 1:

        #Run A*
        path = gameBoard.aStarPQ(startTime)

        if(path):
            #Variables from the AStar Function
            movesPath = path[0]
            expandedNodes = path[1]
            successors = path[2]
            totalTime = path[3]
            #Print the stats for A*
            printStats(movesPath,expandedNodes,successors,totalTime,nValue)

        return

    elif searchType == 2:
        gameBoard.hillclimb(startTime)
        return

    elif searchType == 3:
        #Set random queens
        astar = True

        #Bound
        bound = 0
        #Keep track if we have found a solution
        noSolution = True

        #Keep doing iterative deepining until we find a solution
        while(noSolution):
            newBoard = copy.deepcopy(gameBoard)
            path = newBoard.aStarPQWithIterativeDeepining(startTime,bound)

            if(path is None):
                print("RAN OUT OF TIME")
                return

            elif(not path):
                print("Running A* with iterative deeping with a bigger bound")
                bound += 40

            else:
                print("Solution Found")
                noSolution = path[4]


        #Variables from the AStar Function
        movesPath = path[0]
        expandedNodes = path[1]
        successors = path[2]
        totalTime = path[3]

        #Print the stats for A*
        printStats(movesPath,expandedNodes,successors,totalTime,nValue, astar)

        return

    else:
        print("Make sure to make a valid Search Type")
        return



#Run the main function
if __name__ == "__main__":
    main()
