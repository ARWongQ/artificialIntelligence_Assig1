# work in progress file for hill climbing algorithm - will move to Board class later
import time
import copy

def hillclimb(self):
    print "RUNNING HILLCLIMB"
    # initial conditions
    t_stop = time.time() + 10
    list_endboards = []
    solution_found = False
    # run hillclimb with restarts for 10 seconds (if no solution found yet)
    while time.time() < t_stop and not (solution_found):
        # climb initial conditions
        climb = True
        moves = 1
        # keep climbing until local optimal reached
        while climb:
            self.checkTotalHittingQueens()
            current_h = self.h
            print "CURRENT H: ", self.h
            # break if at solution
            if current_h == 0:
                "FOUND SOLUTION!"
                break
            # calculate h for all
            self.setAllBoardNodesHeuristic()
            self.printBoard()
            # find lowest board
            lowest = self.findlowestH()
            if current_h > lowest[0]:
                # move queen
                for j in xrange(self.dimensions):
                    if (self.grid[lowest[1]][j].queen == True):
                        self.grid[lowest[1]][j].queen = False
                self.grid[lowest[1]][lowest[2]].queen = True
                moves += 1
            else:
                climb = False
    # check if local or global solution
    if current_h > 0:
        print("LOCAL OPTIMAL SOLUTION FOUND\n")
        list_endboards.append(0)
    else:
        solution_found = True
        print("GLOBAL OPTIMAL SOLUTION FOUND\n")
        list_endboards.append(0)
    # reset board
    self.setNewRandomQueens()
    print "# moves = ", moves
# choose best solution out of restarts
# output data

def findlowestH(self):
    # go through each node and find lowest value
    lowest_h = self.h
    low_i = 0
    low_j = 0
    print "Finding lowest H on board"
    for i in xrange(self.dimensions):
        for j in xrange(self.dimensions):
            if (self.grid[i][j].queen != True):
                # compare h value
                if self.grid[i][j].h < lowest_h:
                    lowest_h = self.grid[i][j].h
                    low_i = i
                    low_j = j
                    print"lowest H of ",lowest_h," found at [",i,"]","[",j,"]"
                if self.grid[i][j].h == lowest_h:
                    # come up with random choice
                    print "equal lowest H of ",lowest_h," found at [",i,"]","[",j,"]"
                    pass