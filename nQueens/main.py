import time
from Board import Board
from queenPos import QueenPos

#Main Function
def main():
    print("Running nQueens")

    #Get the n Value and the type of Search for the problem
    nValue = input("N value for the N-queens problem: ")
    searchType = input("Type of Search: 1 for A* and 2 for greedy hill climbing: ")

    #Start the Board
    gameBoard = Board(nValue)
    print(" ")



    if searchType == 1:
        #Set random queens
        gameBoard.setRandomQueensTwo()

        #Start the time
        startTime = time.time()

        #Run A*
        path = gameBoard.aStarPQ()

        #Print the stats
        totalTime = time.time() - startTime

        i = 0
        lastBoardCost = 0
        for currBoard in reversed(path[0]):
            if i == 0:
                print("Starting Board is ----------")
            else:
                print("Step " + str(i) + " ----------")

            currBoard.printBoard()
            i += 1
            #Keep track of the total cost
            lastBoardCost = currBoard.g


        print("It took A* "+ str(totalTime) + " seconds to solve the "+ str(nValue) +"-queens problem")
        print("With Expanded Nodes: " + str(path[1]))
        print("With a branching factor of " + str(path[2]))
        print("And a cost of " + str(lastBoardCost))

        return

    if searchType == 2:
        gameBoard.hillclimb()
        return

    if searchType == 3:
        print("Testing")
        gameBoard.grid[0][0].queen = True
        gameBoard.grid[1][0].queen = True
        gameBoard.grid[2][0].queen = True
        gameBoard.grid[3][0].queen = True
        gameBoard.grid[4][0].queen = True
        gameBoard.grid[5][0].queen = True


        gameBoard.queenPositions.append(QueenPos(0,0))
        gameBoard.queenPositions.append(QueenPos(1,0))
        gameBoard.queenPositions.append(QueenPos(2,0))
        gameBoard.queenPositions.append(QueenPos(3,0))
        gameBoard.queenPositions.append(QueenPos(4,0))
        gameBoard.queenPositions.append(QueenPos(5,0))


        #Start the time
        startTime = time.time()

        #Run A*
        path = gameBoard.aStarPQ()

        #Print the stats
        totalTime = time.time() - startTime

        i = 0
        lastBoardCost = 0
        for currBoard in reversed(path[0]):
            if i == 0:
                print("Starting Board is ----------")
            else:
                print("Step " + str(i) + " ----------")

            currBoard.printBoard()
            i += 1

            lastBoardCost = currBoard.g


        print("It took A* "+ str(totalTime) + " seconds to solve the "+ str(nValue) +"-queens problem")
        print("With Expanded Nodes: " + str(path[1]))
        print("With a branching factor of " + str(path[2]) )
        print("And a cost of " + str(lastBoardCost))



        return

    else:
        print("Make sure to make a valid Search Type")
        return



#Run the main function
if __name__ == "__main__":
    main()
