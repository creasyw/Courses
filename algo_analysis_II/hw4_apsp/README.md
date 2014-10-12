### Question 1
In this assignment you will implement one or more algorithms for the all-pairs shortest-path problem. Here are data files describing three graphs: g1.txt; g2.txt; g3.txt.

The first line indicates the number of vertices and edges, respectively. Each subsequent line describes an edge (the first two numbers are its tail and head, respectively) and its length (the third number). NOTE: some of the edge lengths are negative. NOTE: These graphs may or may not have negative-cost cycles.

Your task is to compute the "shortest shortest path". Precisely, you must first identify which, if any, of the three graphs have no negative cycles. For each such graph, you should compute all-pairs shortest paths and remember the smallest one (i.e., compute ![equation](http://www.sciweavers.org/tex2img.php?eq=min_%7Bu%2Cv%5Cin%20V%7Dd%28u%2C%20v%29%20&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0), where d(u,v) denotes the shortest-path distance from u to v).

If each of the three graphs has a negative-cost cycle, then enter "NULL" in the box below. If exactly one graph has no negative-cost cycles, then enter the length of its shortest shortest path in the box below. If two or more of the graphs have no negative-cost cycles, then enter the smallest of the lengths of their shortest shortest paths in the box below.

OPTIONAL: You can use whatever algorithm you like to solve this question. If you have extra time, try comparing the performance of different all-pairs shortest-path algorithms!

OPTIONAL: If you want a bigger data set to play with, try computing the shortest shortest path for this large.txt.
