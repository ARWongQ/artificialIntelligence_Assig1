Heavy N-Queens Problem
The program will request the user for an N-value which will create the board to be solved (NxN). Then it will request the algorithm to be used in order to solve the n-queens problem. The program can currently use A*, greedy hill climbing and A* with iterative deepening (A*ID). The program will tell the user how long it took to solve the puzzle, the number of expanded nodes, succesors per node, effective branching factor, and the cost to reach the solution. Furthermore, each program will only run for 10seconds before terminating. If the algorithm has not yet found a solution within 10seconds it will display that it has ran out of time and that no solution was found.

If there is no solution, A* will return that there is no optimal solution (2x2, 3x3).

A*                // press 1.

greedy hill       // press 2.

A*ID              // press 3.


Sample Program:

N value for the N-queens problem: 4

Types of Search
 1 for A* and
 2 for greedy hill climbing
 3 for A* with iterative Deepining: 1

The starting Board is ---------

0 0 Q 0

0 Q 0 0

0 0 0 Q

Q 0 0 0

Running A*
We have found a solution

Step 1 ----------
0 0 Q 0

Q 0 0 0

0 0 0 Q

Q 0 0 0


Step 2 ----------

0 0 Q 0

Q 0 0 0

0 0 0 Q

0 Q 0 0

It took A* 0.0871469974518 seconds to solve the 4-queens problem
With Expanded Nodes: 2
With successor per node of 12
With an effective branching factor of 2/2
And a cost of 22
