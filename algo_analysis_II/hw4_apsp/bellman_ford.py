import os, re
import numpy as np
from collections import defaultdict
from dijkstras import buildgraph

finder = re.compile("-?\d+")


def bellman_ford(arr, start, size):
    """ The input arr stores all info of the graph in a dictionary.
        The basic element in the arr are three-columns data -- 
        [start_point, end_point, cost]"""
    count = 1
    data = np.zeros((2, size + 1))
    # initialization
    data.fill(float("inf"))
    data[0, start] = 0

    # major algo
    # bucket for the nodes about to expolre
    # for every "about-to" end point, it only records the smallest cost rount
    # the structure is {... end: [start, cost] ...}
    bucket = {}
    for i in arr[start]:
        bucket[i] = {start: arr[start][i]}

    for i in range(1, size):
        # use set() to make sure the start points in the next round are unique
        candidate = set()
        previous = count ^ 1
        data[count] = data[previous]
        for v in bucket:
            data[count, v] = min(data[previous, v], data[previous, bucket[v].keys()[0]]\
                    + bucket[v].values()[0])
            candidate.add(v)
        # stop early
        if (data[count] == data[previous]).all():
            break
        # update the nodes that are about to explore
        bucket = {}
        for j in candidate:
            for k in arr[j]:
                if (k in bucket and data[count,j]+arr[j][k] < data[count, \
                        bucket[k].keys()[0]]+bucket[k].values()[0]) or k not in bucket:
                    bucket[k] = {}
                    bucket[k][j] = arr[j][k]
        # halt if there is no link between the known cut and the unknown
        if not bucket:
            break
        count = previous
    # check cycle with negative sum
    previous = count ^ 1
    data[count] = data[previous]
    for v in bucket:
        data[count, v] = min(data[previous, v], data[previous, bucket[v].keys()[0]]\
                + bucket[v].values()[0])
    if (data[count] == data[previous]).all():
        return data[count]
    else:
        return float("inf")


def main():
    import sys
    assert len(
        sys.argv) == 3, "The proper input format is: ~$ python SCRIPT.py data_file start_node"
    data = defaultdict(list)
    filename = sys.argv[1]
    start = int(sys.argv[2])
    with open(os.path.join(os.path.dirname(__file__), filename)) as datafile:
        vertex, edge = [int(k) for k in finder.findall(datafile.readline())]
        for row in datafile:
            temp = [int(k) for k in finder.findall(row)]
            data[temp[0]].append(temp)

    print bellman_ford(data, start, vertex)


if __name__ == "__main__":
    main()
