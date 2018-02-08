from Board import Board
from priorityQueue import PriorityQueue

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

    else:
        gameBoard.grid[0][0].queen = True
        gameBoard.grid[1][0].queen = True
        gameBoard.grid[2][0].queen = True

        gameBoard.printBoard()

        allBoards = gameBoard.GetAllSuccessors()

        secondGeneration = allBoards[0].GetAllSuccessors()

        for currBoard in secondGeneration:
            currBoard.printBoard()
            print("The F value of the top Board is: " + str(currBoard.f))
            print("The G value of the top Board is: " + str(currBoard.g))

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
