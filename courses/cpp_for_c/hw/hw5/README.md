###Spec Requirement:

* The player should be able to interact with the program and choose its “color” with blue (or X) going first and red (or O) going second.
* The program should have a convenient interface for entering a move, displaying the board, and then making its own move.
* The program should determine when the game is over and announce the winner.
* For the moving decision, the program evaluates all legal available next moves and select a “best” move.  Each legal move will be evaluated using approximately 1000 or more trials (Monte Carlo simulation). Each trial winds the game forward by randomly selecting successive moves until there is a winner. The trial is counted as a win or loss. The ratio: wins/trials are the AI’s metric for picking which next move to make. In this procedure, the Minmax algorithm and alpha-beta pruning might be used.
* For the complexity, the program should efficiently determine within no more than 2 minutes.
