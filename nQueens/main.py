from Board import Board
from priorityQueue import PriorityQueue
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

    #Set random Queens for the Board and print it to the user
    #gameBoard.setRandomQueens()
    #gameBoard.printBoard()

    #Print the Board without the heuristic (starting state)
    #gameBoard.printBoard()

    #Set all the heuristic of the board
    #gameBoard.setAllBoardNodesHeuristic()

    # Print the Board with the heuristics
    #gameBoard.printBoard()


    # hillclimb test
    """
    gameBoard.printBoard()
    gameBoard.checkTotalHittingQueens()
    print"CURRENT H: ",gameBoard.h
    gameBoard.findlowestH()
    gameBoard.printBoard()
    gameBoard.setAllBoardNodesHeuristic()
    gameBoard.findlowestH()
    """

    if searchType == 2:
        gameBoard.hillclimb()

    if searchType == 1:
        gameBoard.grid[0][0].queen = True
        gameBoard.grid[1][0].queen = True
        gameBoard.grid[2][0].queen = True
        gameBoard.grid[3][0].queen = True
        gameBoard.grid[4][0].queen = True

        #gameBoard.grid[2][0].queen = True
        #gameBoard.grid[3][0].queen = True
        #gameBoard.grid[4][0].queen = True

        gameBoard.queenPositions.append(QueenPos(0,0))
        gameBoard.queenPositions.append(QueenPos(1,0))
        gameBoard.queenPositions.append(QueenPos(2,0))
        gameBoard.queenPositions.append(QueenPos(3,0))
        gameBoard.queenPositions.append(QueenPos(4,0))

        gameBoard.aStarPQ()
        return

    if searchType == 3:
        gameBoard.grid[0][0].queen = True
        gameBoard.grid[1][0].queen = True

        gameBoard.queenPositions.append(QueenPos(0,0))
        gameBoard.queenPositions.append(QueenPos(1,0))

        gameBoardTwo = Board(nValue)
        gameBoardTwo.grid[0][0].queen = True
        gameBoardTwo.grid[1][0].queen = True

        gameBoardTwo.queenPositions.append(QueenPos(0,0))
        gameBoardTwo.queenPositions.append(QueenPos(1,0))

        gameBoardThree = Board(nValue)
        gameBoardThree.grid[0][0].queen = True
        gameBoardThree.grid[1][1].queen = True

        gameBoardThree.queenPositions.append(QueenPos(0,0))
        gameBoardThree.queenPositions.append(QueenPos(1,1))


        list = []
        list.append(gameBoardTwo)
        list.append(gameBoardThree)


        isInList = gameBoard.checkBoardInList(list)
        print("The value is " + str(isInList))

        if(isInList == True):
            print("They are the same")
        else:
            print("They are not the same")





    else:
        gameBoard.grid[0][0].queen = True
        gameBoard.grid[1][0].queen = True
        gameBoard.grid[2][0].queen = True
        gameBoard.queenPositions.append(QueenPos(0,0))
        gameBoard.queenPositions.append(QueenPos(1,0))
        gameBoard.queenPositions.append(QueenPos(2,0))


        gameBoard.printBoard()
        for currQueenPos in gameBoard.queenPositions:
            print("The Main Board has queens in " + str(currQueenPos.i) + str(currQueenPos.j))

        gameBoard.neighbors = gameBoard.GetAllSuccessors()


        #gameBoard.neighbors[0].neighbors = gameBoard.neighbors[0].GetAllSuccessors()

        for currBoard in gameBoard.neighbors:
            currBoard.printBoard()
            print("The F value of the top Board is: " + str(currBoard.f))
            print("The G value of the top Board is: " + str(currBoard.g))
            print("The h value of the top Board is: " + str(currBoard.h))
            for currQueenPos in currBoard.queenPositions:
                print("The Queen is in " + str(currQueenPos.i) + str(currQueenPos.j) )


        """
        allBoardPQ = PriorityQueue()

        for currBoard in allBoards:
            allBoardPQ.push(currBoard,currBoard.f)

        BestBoard = allBoardPQ.pop()
        BestBoard.printBoard()

        BestBoard2 = allBoardPQ.pop()
        BestBoard2.printBoard()
        """





    #Get the heuristic of the board after calculating all the node's heuristic
    #gameBoard.checkTotalHittingQueens()

    #Print the heurstic of the queens
    #hitting = gameBoard.h
    #print("These many queens are hitting each other")
    #print(hitting)




#Run the main function
if __name__ == "__main__":
    main()
