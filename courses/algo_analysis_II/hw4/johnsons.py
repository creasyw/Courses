import os, re
import numpy as np
from collections import defaultdict
# import other algorithm
from dijkstras import dijkstras
from bellman_ford import bellman_ford

finder = re.compile("-?\d+")

def johonsons(data, vertex):
    new = vertex+1
    data[new] = [[new, k, 0] for k in range(1, new)]
    print bellman_ford(data, new, new)
    

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
    johonsons(data, vertex)

if __name__ == "__main__":
    main()



