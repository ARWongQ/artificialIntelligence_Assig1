from Board import Board

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
    gameBoard.setRandomQueens()

    #Print the Board without the heuristic
    gameBoard.printBoard()

    #Set all the heuristic of the board
    gameBoard.setAllBoardNodesHeuristic()

    """
    hillclimb test
    gameBoard.printBoard()
    gameBoard.checkTotalHittingQueens()
    print"CURRENT H: ",gameBoard.h
    gameBoard.findlowestH()
    """
    """
    if searchType == 2:
        gameBoard.hillclimb()
    """

    #Print the Board with the heuristics
    gameBoard.printBoard()

    #Get the heuristic of the board after calculating all the node's heuristic
    gameBoard.checkTotalHittingQueens()



    #Print the heurstic of the queens
    hitting = gameBoard.h
    print("These many queens are hitting each other")
    print(hitting)




#Run the main function
if __name__ == "__main__":
    main()
