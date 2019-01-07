
The file format is as follows. In each instance, the number of variables and the number of clauses is the same, and this number is specified on the first line of the file. Each subsequent line specifies a clause via its two literals, with a number denoting the variable and a "-" sign denoting logical "not". For example, the second line of the first data file is "-16808 75250", which indicates the clause ¬x16808∨x75250.

The task is to determine which of the 6 instances are satisfiable, and which are unsatisfiable. In the box below, enter a 6-bit string, where the ith bit should be 1 if the ith instance is satisfiable, and 0 otherwise. For example, if you think that the first 3 instances are satisfiable and the last 3 are not, then you should enter the string 111000 in the box below.

Concerning the solution:
* 2SAT reduces to computing the strongly connected components of a suitable graph (with two vertices per variable and two directed edges per clause). This might be an especially attractive option to use SCC algorithm.  
* Alternatively, Papadimitriou's randomized local search algorithm is applicable. (The naive algorithm might be too slow, so one or more simple modifications are necessary to ensure that it runs in a reasonable amount of time.)  
* A third approach is via backtracking. Refer the [DPV book](http://www.cs.berkeley.edu/~vazirani/algorithms/chap9.pdf) for more details.
