from Board import Board

#Main Function
def main():
    print("Running nQueens")

    #Get the n Value and the type of Search for the problem
    nValue = input("N value for the N-queens problem: ")
    searchType = input("Type of Search: 1 for A* and 2 for greedy hill climbing: ")

    gameBoard = Board(nValue)
    print(" ")

    gameBoard.setRandomQueens()
    gameBoard.printBoard()

    hitting = gameBoard.checkTotalHittingQueens()

    print("These many queens are hitting each other")
    print(hitting)




#Run the main function
if __name__ == "__main__":
    main()
