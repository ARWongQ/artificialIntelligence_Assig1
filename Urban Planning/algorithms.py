import time
import UPGetScore
import UPParser
import copy
import math
import random
import UrbanMap
from priorityQueue import PriorityQueue

# Runs Greed Hill Climb algorithm
def hillClimb(startingMap):
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
            nextScore,nn,nextMap = nodePQueue.pop()

            # Save node path
            nextMap.previous = currentMap

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
    maxTime = 10
    finalMap = None
    timeOfBest = 0
    bestScore = -10000000
    genCnt = 0
    maxInGeneration = 100
    maxCull = int(math.ceil(maxInGeneration/10))
    maxElite = maxCull
    currentGen = PriorityQueue()

    # Start timing
    startTime = time.time()

    # Randomly assign values
    for i in range(maxInGeneration):
        newMap = copy.deepcopy(map)
        newMap.randAssign()
        currentGen.push(newMap,UPGetScore.getMapScore(newMap))

    # Begin generation while loop
    while (time.time() - startTime < maxTime):
        nextGen = PriorityQueue()
        genCnt += 1
        # print("Beginning Generation: " + str(genCnt))

        # Save elite nodes to next gen
        for i in range(maxElite):
            eliteScore,nn,eliteMap = currentGen.pop()
            nextGen.push(eliteMap,eliteScore)

        # Cull nodes in currentGen
        for i in range(maxCull):
            currentGen.popMin()

        # Pick combination of nodes to cross and add children to nextGen
        oddsList = []
        for i in range(len(currentGen)):
            for j in range(i+1):
                oddsList.append(i)

        # Fill next generation while loop
        while(len(nextGen) < maxInGeneration):
            rand = random.randint(0,len(oddsList)-1)
            rand2 = rand
            while(oddsList[rand2] == oddsList[rand]):
                rand2 = random.randint(0,len(oddsList)-1)
            # print("Crossing " + str(oddsList[rand]) + " and " + str(oddsList[rand2]))
            crossingMaps = []
            crossingMaps.append(currentGen[oddsList[rand]][2])
            crossingMaps.append(currentGen[oddsList[rand2]][2])

            merge1, merge2 = mergeMaps(crossingMaps[0],crossingMaps[1])

            nextGen.push(merge1,UPGetScore.getMapScore(merge1))
            if(len(nextGen) < maxInGeneration):
                nextGen.push(merge2, UPGetScore.getMapScore(merge2))

        # End fill generation while loop

        # Set best from queue as best map
        possibleBestScore, nn, possibleFinalMap = nextGen[len(nextGen)-1]
        if(possibleBestScore > bestScore):
            bestScore = possibleBestScore
            finalMap = possibleFinalMap
            timeOfBest = time.time() - startTime
            bestGen = genCnt

        currentGen = nextGen

    # End random restart while loop

    return bestScore, timeOfBest, finalMap, bestGen


def mergeMaps(map1, map2):
    rFromMap1, iFromMap1, cFromMap1 = map1.findRICIndivid()
    rFromMap2, iFromMap2, cFromMap2 = map2.findRICIndivid()

    if (len(rFromMap1) == 0):
        print("Empty R")
        exit(1)
    if(len(iFromMap1) == 0):
        print("Empty I")
        exit(1)
    if (len(cFromMap1) == 0):
        print("Empty C")
        exit(1)

    newMap1 = UrbanMap.UrbanMap(map1.R,map1.I,map1.C,copy.deepcopy(map1.map))
    newMap2 = UrbanMap.UrbanMap(map2.R, map2.I, map2.C, copy.deepcopy(map2.map))

    randSwitch = random.randint(1,3)

    if(randSwitch == 1):
        newMap1, newMap2 = updateValues(rFromMap1, rFromMap2, newMap1, newMap2, 'R')
    elif(randSwitch == 2):
        newMap1, newMap2 = updateValues(iFromMap1, iFromMap2, newMap1, newMap2, 'I')
    else: # randSwitch == 3
        newMap1, newMap2 = updateValues(cFromMap1, cFromMap2, newMap1, newMap2, 'C')

    return newMap1, newMap2


def updateValues(valFromMap1,valFromMap2,newMap1,newMap2,Val):

    for i in range(len(valFromMap1)):
        # print("Removing " + Val + " from map1")
        coord = valFromMap1[i]
        if (newMap1.map[coord[0]][coord[1]][0] == 'S'):
            newMap1.map[coord[0]][coord[1]][1] = 'S'
        else:
            newMap1.map[coord[0]][coord[1]][1] = '-'

    for i in range(len(valFromMap2)):

        coord2 = valFromMap2[i]
        if ((newMap1.map[coord2[0]][coord2[1]][1] == '-') | (newMap1.map[coord2[0]][coord2[1]][1] == 'S')):
            # print("Adding " + Val + " to map1 at Row:" + str(coord2[0]) + " Col: " + str(coord2[1]))
            newMap1.map[coord2[0]][coord2[1]][1] = Val
        else:  # mutate
            while ((newMap1.map[coord2[0]][coord2[1]][1] == 'X') | (newMap1.map[coord2[0]][coord2[1]][1] == 'I') | (newMap1.map[coord2[0]][coord2[1]][1] == 'R') | (newMap1.map[coord2[0]][coord2[1]][1] == 'C')):
                # print("Mutating for " + Val)
                coord2 = [random.randint(0, len(newMap1.map)-1), random.randint(0, len(newMap1.map[0])-1)]
            # print("Replacing: " + newMap1.map[coord2[0]][coord2[1]][1] + " at Row:" + str(coord2[0]) + " Col: " + str(coord2[1]))
            newMap1.map[coord2[0]][coord2[1]][1] = Val

    for i in range(len(valFromMap2)):
        # print("Removing " + Val + " from map2")
        coord2 = valFromMap2[i]
        if (newMap2.map[coord2[0]][coord2[1]][0] == 'S'):
            newMap2.map[coord2[0]][coord2[1]][1] = 'S'
        else:
            newMap2.map[coord2[0]][coord2[1]][1] = '-'

    for i in range(len(valFromMap1)):

        coord = valFromMap1[i]
        if ((newMap2.map[coord[0]][coord[1]][1] == '-') | (newMap2.map[coord[0]][coord[1]][1] == 'S')):
            # print("Adding " + Val + " to map2 at Row:" + str(coord[0]) + " Col: " + str(coord[1]))
            newMap2.map[coord[0]][coord[1]][1] = Val
        else:  # mutate
            while ((newMap2.map[coord[0]][coord[1]][1] == 'X') | (newMap2.map[coord[0]][coord[1]][1] == 'I') | (newMap2.map[coord[0]][coord[1]][1] == 'R') | (newMap2.map[coord[0]][coord[1]][1] == 'C')):
                # print("Mutating for " + Val)
                coord = [random.randint(0, len(newMap2.map)-1), random.randint(0, len(newMap2.map[0])-1)]
            # print("Replacing: " + newMap2.map[coord[0]][coord[1]][1] + " at Row:" + str(coord[0]) + " Col: " + str(coord[1]))
            newMap2.map[coord[0]][coord[1]][1] = Val

    return newMap1, newMap2

