import os
import re
import numpy as np
from union_find import union_find

finder = re.compile("-?\d+")

def diff(a, b):
    return sum(1 for k in range(len(a)) if a[k]!=b[k])

def put_point(x, p, threshold):
    found = False
    keys = x.all_keys()
    for i in keys:
        if not found and diff(i, p) < threshold:
            x.alldata[p] = x.alldata[i]
            x.cluster[x.alldata[i]].append(p)
            found = True
        if found and x.alldata[i] != x.alldata[p] and diff(i,p)<threshold:
            x.union(x.alldata[i], x.alldata[p])
    if not found:
        x.alldata[p] = p
        x.cluster[p] = [p]

def iterate(data):
    x = union_find()
    [put_point(x, k, 3) for k in data]
    print x.length()

def main():
    temp = []
    with open(os.path.join(os.path.dirname(__file__), "clustering_big.txt")) as datafile:
        num_of_nodes, digits = [int(k) for k in finder.findall(datafile.readline())]
        for row in datafile:
            temp.append("".join(finder.findall(row)))
    iterate(temp)

if __name__ == "__main__":
    main()
