import UPParser
import UPGetScore
from UrbanMap import UrbanMap
import algorithms

#Main Function
def main():
    print("Running Urban Planning")

    # Receive input
    # searchType = raw_input("Type of Search: 1 for greedy hill climbing and 2 for genetic: ")
    # fileName = raw_input("File path for map: ")

    searchType = "1";
    fileName = "sample 2.txt"

    # Load from file
    map = UPParser.parseUrbanMap(fileName)

    # Print map info
    UPParser.printMapNicely(map)

    if(int(searchType) == 1): # if greedy hill climb
        print("Beginning Greedy Hill Climb Algorithm")
        bestScore, timeOfBest, finalMap = algorithms.hillClimb(map)
    else: # else genetic
        print("Beginning Genetic Algorithm")
        algorithms.genetic(map)

    print("The score for this map: " + str(bestScore))
    print("Time of achieval: " + str(timeOfBest))
    print("Final map: ")
    UPParser.printMapNicely(finalMap)

#Run the main function
if __name__ == "__main__":
    main()
