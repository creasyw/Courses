import os, re
import numpy as np
from collections import defaultdict
# import other algorithm
from dijkstras import dijkstras, buildgraph
from bellman_ford import bellman_ford

finder = re.compile("-?\d+")


def reconvert(reweight, vertex, dij, start):
    for i in range(1, vertex + 1):
        if i in dij:
            dij[i] = dij[i] - reweight[start] + reweight[i]
        else:
            dij[i] = float("inf")
    return dij.values()


def johonsons(data, vertex):
    d1 = data.copy()
    # make psedu node pointing to all other nodes with zero cost
    plus1 = vertex + 1
    d1[plus1] = {}
    for i in range(1, plus1):
        d1[plus1][i] = 0
    # calculate the reweight vector
    reweight = bellman_ford(d1, plus1, plus1)
    # reweight all cost to make it nonnegative
    if type(reweight) == float:
        # stop if there is any negative cycle in the graph
        return None
    else:
        for i in data:
            for k in data[i]:
                data[i][k] = data[i][k] + reweight[i] - reweight[k]
    result = []
    return [min(reconvert(reweight,vertex,dijkstras(data,i),i))\
                        for i in range(1,vertex+1)]


def main():
    import sys
    assert len(
        sys.argv) == 2, "The proper input format is: ~$ python SCRIPT.py data_file"
    data = defaultdict(list)
    filename = sys.argv[1]
    with open(os.path.join(os.path.dirname(__file__), filename)) as datafile:
        vertex, edge = [int(k) for k in finder.findall(datafile.readline())]
        for row in datafile:
            temp = [int(k) for k in finder.findall(row)]
            data[temp[0]].append(temp)
    print min(johonsons(buildgraph(data), vertex))


if __name__ == "__main__":
    main()

# The comprehensive test case is from ../hw1/edges.txt
# -435795
