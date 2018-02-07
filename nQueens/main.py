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
    gameBoard.printBoard()

    #Check how many queens are hitting each other
    gameBoard.checkTotalHittingQueens()


    #Print the heurstic of the queens
    hitting = gameBoard.h
    print("These many queens are hitting each other")
    print(hitting)




#Run the main function
if __name__ == "__main__":
    main()
