# noinspection SpellCheckingInspection,PyUnusedLocal,PyTrailingSemicolon

import UPGetScore
from priorityQueue import PriorityQueue
import random
import copy

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

        ricList = self.findRIC()

        for nn in range(len(ricList)):
            # Add left
            leftMap = self.moveLeft(ricList[nn])
            if(leftMap != None):
                PQ.push(leftMap,UPGetScore.getMapScore(leftMap))

            # Add right
            rightMap = self.moveRight(ricList[nn])
            if(rightMap != None):
                PQ.push(rightMap, UPGetScore.getMapScore(rightMap))

            # Add up
            upMap = self.moveUp(ricList[nn])
            if(upMap != None):
                PQ.push(upMap, UPGetScore.getMapScore(upMap))

            # Add down
            downMap = self.moveDown(ricList[nn])
            if(downMap != None):
                PQ.push(downMap, UPGetScore.getMapScore(downMap))

        return PQ


    def findRIC(self):
        pos = []
        for row in range(len(self.map)):
            for col in range(len(self.map[0])):
                if((self.map[row][col][1] == 'R') | (self.map[row][col][1] == 'I') | (self.map[row][col][1] == 'C')):
                    pos.append([row,col])

        return pos


    def moveLeft(self,coords):
        map = copy.deepcopy(self.map)

        newMap = UrbanMap(self.R,self.I,self.C,map)
        newMap.previous = self

        if(coords[1]-1 >= 0):
            if((newMap.map[coords[0]][coords[1]-1][1] == '-') | (newMap.map[coords[0]][coords[1]-1][1] == 'S')):
                newMap.map[coords[0]][coords[1]-1][1] = newMap.map[coords[0]][coords[1]][1]
                if (newMap.map[coords[0]][coords[1]][0] == 'S'):
                    newMap.map[coords[0]][coords[1]][1] = 'S'
                else:
                    newMap.map[coords[0]][coords[1]][1] = '-'
        else:
            newMap = None

        return newMap


    def moveRight(self,coords):
        map = copy.deepcopy(self.map)

        newMap = UrbanMap(self.R, self.I, self.C, map)
        newMap.previous = self

        if (coords[1] + 1 < len(self.map[0])):
            if((newMap.map[coords[0]][coords[1]+1][1] == '-') | (newMap.map[coords[0]][coords[1]+1][1] == 'S')):
                newMap.map[coords[0]][coords[1]+1][1] = newMap.map[coords[0]][coords[1]][1]
                if (newMap.map[coords[0]][coords[1]][0] == 'S'):
                    newMap.map[coords[0]][coords[1]][1] = 'S'
                else:
                    newMap.map[coords[0]][coords[1]][1] = '-'
        else:
            newMap = None

        return newMap


    def moveUp(self,coords):
        map = copy.deepcopy(self.map)

        newMap = UrbanMap(self.R, self.I, self.C, map)
        newMap.previous = self

        if (coords[0] - 1 >= 0):
            if((newMap.map[coords[0]-1][coords[1]][1] == '-') | (newMap.map[coords[0]-1][coords[1]][1] == 'S')):
                newMap.map[coords[0]-1][coords[1]][1] = newMap.map[coords[0]][coords[1]][1]
                if (newMap.map[coords[0]][coords[1]][0] == 'S'):
                    newMap.map[coords[0]][coords[1]][1] = 'S'
                else:
                    newMap.map[coords[0]][coords[1]][1] = '-'
        else:
            newMap = None

        return newMap


    def moveDown(self,coords):
        map = copy.deepcopy(self.map)

        newMap = UrbanMap(self.R, self.I, self.C, map)
        newMap.previous = self

        if (coords[0] + 1 < len(self.map)):
            if((newMap.map[coords[0]+1][coords[1]][1] == '-') | (newMap.map[coords[0]+1][coords[1]][1] == 'S')):
                newMap.map[coords[0]+1][coords[1]][1] = newMap.map[coords[0]][coords[1]][1]
                if(newMap.map[coords[0]][coords[1]][0] == 'S'):
                    newMap.map[coords[0]][coords[1]][1] = 'S'
                else:
                    newMap.map[coords[0]][coords[1]][1] = '-'
        else:
            newMap = None

        return newMap




    def randAssign(self):
        # print("Setting random assignments")

        openCoordinates = []
        for row in range(len(self.map)):
            for col in range(len(self.map[0])):
                if((self.map[row][col][1] == '-') | (self.map[row][col][1] == 'S')):
                    openCoordinates.append([row,col])

        for i in range(self.R):
            coord = random.randint(0,len(openCoordinates)-1)
            rCoord = openCoordinates.pop(coord)
            self.map[rCoord[0]][rCoord[1]][1] = 'R'

        for i in range(self.I):
            coord = random.randint(0,len(openCoordinates)-1)
            iCoord = openCoordinates.pop(coord)
            self.map[iCoord[0]][iCoord[1]][1] = 'I'

        for i in range(self.C):
            coord = random.randint(0,len(openCoordinates)-1)
            cCoord = openCoordinates.pop(coord)
            self.map[cCoord[0]][cCoord[1]][1] = 'C'

