###Spec Requirement:

* The player should be able to interact with the program and choose its “color” with blue (or X) going first and red (or O) going second.
* The program should have a convenient interface for entering a move, displaying the board, and then making its own move.
* The program should determine when the game is over and announce the winner.
* For the moving decision, the program evaluates all legal available next moves and select a “best” move.  Each legal move will be evaluated using approximately 1000 or more trials (Monte Carlo simulation). Each trial winds the game forward by randomly selecting successive moves until there is a winner. The trial is counted as a win or loss. The ratio: wins/trials are the AI’s metric for picking which next move to make. In this procedure, the Minmax algorithm and alpha-beta pruning might be used.
* For the complexity, the program should efficiently determine within no more than 2 minutes.

###Some hints from discussion board:
* using
````
g++ -O3 -Wall -c -fmessage-length=0 -std=c++11 ...
````
to accelerate the compiled program. For more options, refer to [GCC - Options That Control Optimization](http://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html).
* Take 4 by 4 board for example. There are 16! orderings for filling the board, but at the end of a game the order of tokens is indistinguishable. So, both color has 8! deduction. Furthermore, the board is "mirror-symmetric" along the diagonal. Hence, there are 16!/8!/8!/2=6435 different arrangements for a Monte Carlo simulation.
* It is unnecessary to fill both players. Fill one players for the half the rest positions, then it is ready to check for winner. And there is one and only one winner for each trail.
* To perform 1000 Monte Carlo simulation for every move, the "copy-current-state" might be the bottleneck of performace for a large board. Try to use "shallow copy" or a vector of move, which starts from the current state, stops as either side wins, and then performs rollback.
* The union-find algorithm should be "incrementable" to decide the winner.
* A possible roadmap:
    * Write a class that does random valid moves automatically.
    * Write a class that iterates over all free cells, make MC evaluations everywhere and makes the best possible moves.
    * Look more moves into the future using Min-Max (refine the "best possible" move).
    * Optimize Min-Max using Alpha-Beta.
    * Try to further optimize.
