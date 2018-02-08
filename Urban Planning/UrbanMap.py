# noinspection SpellCheckingInspection,PyUnusedLocal,PyTrailingSemicolon

import UPGetScore
from priorityQueue import PriorityQueue
import random

# The class for the map
class UrbanMap:
    def __init__(self, r, i, c, map):
        self.R = r
        self.I = i
        self.C = c
        self.map = map
        self.previous = None


    def hillClimb(self):
        PQ = PriorityQueue()
        PQ.push(self,UPGetScore.getMapScore(self))
        return PQ


    def randAssign(self):
        print("Setting random assignments")

        openCoordinates = []
        for row in range(len(self.map)):
            for col in range(len(self.map[0])):
                if(self.map[row][col][1] == '-'):
                    openCoordinates.append([row,col])

        for i in range(self.R):
            print("Adding an R")
            coord = random.randint(0,len(openCoordinates)-1)
            rCoord = openCoordinates.pop(coord)
            print(rCoord)
            self.map[rCoord[0]][rCoord[1]][1] = 'R'

        for i in range(self.I):
            print("Adding an I")
            coord = random.randint(0,len(openCoordinates)-1)
            iCoord = openCoordinates.pop(coord)
            print(iCoord)
            self.map[rCoord[0]][rCoord[1]][1] = 'I'

        for i in range(self.C):
            print("Adding a C")
            coord = random.randint(0,len(openCoordinates)-1)
            cCoord = openCoordinates.pop(coord)
            print(cCoord)
            self.map[rCoord[0]][rCoord[1]][1] = 'C'

