# work in progress file for hill climbing algorithm - will move to Board class later
import time
import copy

def hillclimb(self):
    # initial conditions
    t_stop = time.time() + 10
    climb = True
    solution_found = False
    moves = 0
    list_endboards = []
    # run hillclimb with restarts for 10 seconds (if no solution found yet)
    while time.time() < t_stop and not(solution_found) :
        # keep climbing until local optimal reached
        while climb:
            self.checkTotalHittingQueens()
            current_h = self.h
            # calculate h for all
            self.setAllBoardNodesHeuristic()
            # find lowest board
            lowest = findlowestH(self)
            if current_h > lowest[0]:
                # move queen
                for j in xrange(self.dimensions):
                    if (self.grid[lowest[1]][j].queen == True):
                        self.grid[lowest[1]][j].queen = False
                self.grid[lowest[1]][lowest[2]].queen == True
                self.checkTotalHittingQueens()
                moves += 1
            else:
                climb = False
        # calculate final heuristic value
        end_h = self.checkTotalHittingQueens()
        # check if local or global solution
        if end_h > 0:
            print("LOCAL OPTIMAL SOLUTION FOUND\n")
            list_endboards.append(0)
        else:
            solution_found = True
            print("GLOBAL OPTIMAL SOLUTION FOUND\n")
            list_endboards.append(0)
        # reset board
        self.setNewRandomQueens()
    # choose best solution out of restarts
    # output data


def findlowestH(self):
    # Loop through the entire Board and find lowest value
    lowest_h = self.h
    low_i = 0
    low_j = 0
    for i in xrange(self.dimensions):
        for j in xrange(self.dimensions):
            if (self.grid[i][j].queen != True):
                # compare h value
                if self.grid[i][j].h < lowest_h:
                    lowest_h = self.grid[i][j].h
                    low_i = i
                    low_j = j
    return (lowest_h, low_i, low_j)


