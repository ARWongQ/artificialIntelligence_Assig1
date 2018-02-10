import time
import UPGetScore
import copy
import UrbanMap
from priorityQueue import PriorityQueue

# Runs Greed Hill Climb algorithm
def hillClimb(startingMap):
    currentScore = -10000000
    maxTime = 10
    finalMap = None
    timeOfBest = 0
    bestScore = -10000000
    cnt = 0

    # Start timing
    startTime = time.time()

    # Begin random restart while loop
    while(time.time() - startTime < maxTime):
        cnt+=1
        print("New Hill Climb Iteration: " + str(cnt))
        # Randomly assign values
        currentMap = copy.deepcopy(startingMap)
        currentMap.randAssign()

        currentScore = -10000000
        innerCnt = 0
        # Begin hill climbing while loop
        while(time.time() - startTime < maxTime):
            innerCnt+=1
            # Determine all possible nodes w/score
            nodePQueue = currentMap.hillClimb()

            # Take map w/ greatest score
            n,nn,nextMap = nodePQueue.pop()

            # Save node path
            nextMap.previous = currentMap

            nextScore = UPGetScore.getMapScore(nextMap)

            if(currentScore < nextScore):
                currentScore = nextScore
                currentMap = nextMap
            else:
                break
        # End hill climbing while loop
        print("Hill climbing went through " + str(innerCnt) + " states")
        # If currentScore is greater than bestScore, replace
        if(currentScore > bestScore):
            bestScore = currentScore
            timeOfBest = time.time() - startTime
            finalMap = currentMap
    # End random restart while loop

    return bestScore, timeOfBest, finalMap


def genetic(map):
    timeOver = 0
    # Start timing
    startTime = time.time()

    # Randomly assign values
    map.randAssign()

    # Begin random restart while loop
    while (time.time() - startTime < 10):
        break