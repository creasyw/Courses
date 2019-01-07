import os, re
import numpy as np
from math import sqrt
from itertools import combinations
import operator

finder = re.compile("-?\d+\.?\d*")


def gen_name(lst):
    return reduce(lambda i, j: i + str(j), sorted(lst), '')


def post_processing(half_way, old, graph, dict):
    candidates = half_way.copy()
    bucket = {}
    for i in candidates:
        this = [0]
        match = gen_name(list((set(range(len(graph))) - set(half_way[i].keys())
                               ) | set(this)))
        if len(graph) % 2 == 1:
            distance = min(candidates[i][m] + candidates[match][n] + \
                    dict[m, n] for m in candidates[i] for n in candidates[match])
        else:
            distance = min(candidates[i][m] + old[match][n] + \
                    dict[m, n] for m in candidates[i] for n in old[match])
        bucket[distance] = [i, match]
    # return the two unoverlapped rountes with mininum summation
    return min(bucket)


def tsp(graph):
    # precompute the distance between nodes
    dict = np.zeros((len(graph), len(graph)))
    for i in range(len(graph)):
        for j in range(i + 1):
            dict[i][j] = dict[j][i] = \
                    sqrt((graph[i][0]-graph[j][0])**2 + \
                    (graph[i][1]-graph[j][1])**2)
    # initialize the starting array
    old = {}
    old['0'] = {0: 0}
    m = 2

    while True:
        current = filter(lambda x: 0 in x, combinations(range(len(graph)), m))
        current_dict = {}
        for s in current:
            cur_name = gen_name(s)
            current_dict[cur_name] = {}
            for j in s:
                if j == 0: continue
                temp = list(s)
                temp.remove(j)
                old_name = gen_name(temp)
                current_dict[cur_name][j] = min(old[old_name][k] + dict[k, j]
                                                for k in temp if k != j)
            current_dict[cur_name][0] = float('inf')
        m += 1
        if m >= len(graph) / 2 + 2: break
        old = current_dict
    # To use dynamic programming exploring TSP, as it calculate smallest distance for N/2 vertex,
    # actually, the problem has already be solved. Because the other half also has already in the
    # dataset.
    return post_processing(current_dict, old, graph, dict)


def main():
    import sys
    assert len(
        sys.argv) == 2, "The proper input format is: ~$ python SCRIPT.py data_file start_node"
    filename = sys.argv[1]
    data = []
    with open(os.path.join(os.path.dirname(__file__), filename)) as datafile:
        num = int(datafile.readline())
        for row in datafile:
            data.append([float(k) for k in finder.findall(row)])

    print tsp(np.array(data))


if __name__ == "__main__":
    main()
