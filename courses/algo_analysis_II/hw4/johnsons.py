import os, re
import numpy as np
from collections import defaultdict
# import other algorithm
from dijkstras import dijkstras, buildgraph
from bellman_ford import bellman_ford

finder = re.compile("-?\d+")

def reconvert(reweight, vertex, dij, start):
    for i in range(1, vertex+1):
        if i in dij:
            dij[i] = dij[i]-reweight[start]+reweight[i]
        else:
            dij[i] = float("inf")
    return dij.values()


def johonsons(data, vertex):
    new = vertex+1
    d1 = data.copy()
    d1[new] = [[new, k, 0] for k in range(1, new)]
    reweight = bellman_ford(d1, new, new)
    if type(reweight) == float:
        return None
    else:
        for i in data:
            data[i] = [[i, data[i][k][1], data[i][k][2]+reweight[i]-reweight[data[i][k][1]]]\
                    for k in range(len(data[i]))]
    graph = buildgraph(data)
    result = []
    for i in range(1, vertex+1):
        result.append(min(reconvert(reweight, vertex, dijkstras(graph, i), i)))
    return min(result)


def main():
    import sys
    assert len(sys.argv)==2, "The proper input format is: ~$ python SCRIPT.py data_file"
    data = defaultdict(list)
    filename = sys.argv[1]
    with open(os.path.join(os.path.dirname(__file__), filename)) as datafile:
            vertex, edge = [int(k) for k in finder.findall(datafile.readline())]
            for row in datafile:
                temp = [int(k) for k in finder.findall(row)]
                data[temp[0]].append(temp)
    print johonsons(data, vertex)

if __name__ == "__main__":
    main()



