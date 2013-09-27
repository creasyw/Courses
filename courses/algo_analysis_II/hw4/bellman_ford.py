import os, re
import numpy as np
from collections import defaultdict

finder = re.compile("-?\d+")

def bellman_ford (arr, start, size):
    """ The input arr stores all info of the graph in a dictionary.
        The key of the dict is vertex and values are two columns list,
        storing the destination and the cost"""
    count = 1
    data = np.zeros((2, size+1))
    # initialization
    data.fill(float("inf"))
    data[0, start] = 0
    
    # major algo
    bucket = arr[start]
    for i in range(1, size):
        candidate = set()
        previous = count ^ 1
        data[count] = data[previous]
        for j in bucket:
            data[count, j[1]] = min( data[previous, j[1]], data[previous, j[0]]+j[2])
            candidate.add(j[1])
        # stop early
        if (data[count]==data[previous]).all():
            break
        new_bucket = []
        for j in candidate:
            new_bucket += arr[j]
        bucket = new_bucket
        if not bucket:
            break
        count = previous
    
    # check cycle with negative sum
    previous = count ^ 1
    for j in bucket:
        data[count, j[1]] = min( data[previous, j[1]], data[previous, j[0]]+j[2])
    if (data[count]== data[previous]).all():
        return data[count]
    else:
        return float("inf")


def main():
    import sys
    assert len(sys.argv)==3, "The proper input format is: ~$ python SCRIPT.py data_file start_node"
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

        

