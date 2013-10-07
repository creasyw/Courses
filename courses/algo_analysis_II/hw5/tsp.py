import os, re
import numpy as np
from math import sqrt
from itertools import combinations
import operator

finder = re.compile("-?\d+\.?\d*")

def gen_name(lst):
    return reduce(lambda i, j: i+str(j), sorted(lst), '')

def post_processing (half_way, graph, dict):
    candidates = half_way.copy()
    full_name = gen_name(range(len(graph)))
    bucket = {}
    for i in candidates:
        candidates[i] = sorted(candidates[i].iteritems(), key=operator.itemgetter(1))
    for i in candidates:
        if len(graph)%2 == 1:
            this = [0]
        else:
            this = [0, candidates[i][0][0]]
        match = gen_name(list( (set(range(len(graph))) - set(half_way[i].keys())) | set(this)))
        distance = candidates[i][0][1] + candidates[match][0][1] + \
                dict[candidates[i][0][0], candidates[match][0][0]]
        bucket[distance] = [i, match]
    # return the two unoverlapped rountes with mininum summation
    return min(bucket)



def tsp(graph):
    # precompute the distance between nodes
    dict = np.zeros((len(graph), len(graph)))
    for i in range(len(graph)):
        for j in range(i+1):
            dict[i][j] = dict[j][i] = \
                    sqrt((graph[i][0]-graph[j][0])**2 + \
                    (graph[i][1]-graph[j][1])**2)
    # initialize the starting array
    old = {}
    old['0'] = {0:0}

    #for m in range(2, len(graph)+1):
    for m in range(2, len(graph)/2+2):
#        print "\n\n Now it is the %s iteration"%(m)
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
                current_dict[cur_name][j] = min(old[old_name][k]+dict[k,j] for k in temp if k!=j)
            current_dict[cur_name][0] = float('inf')
        old = current_dict
    return post_processing(current_dict, graph, dict)

    # go back to the start point and return the smallest result
    #return min(current_dict[cur_name][j]+dict[j,0] for j in range(1, len(graph)))

def main():
    import sys
    assert len(sys.argv)==2, "The proper input format is: ~$ python SCRIPT.py data_file start_node"
    filename = sys.argv[1]
    data = []
    with open(os.path.join(os.path.dirname(__file__), filename)) as datafile:
            num = int(datafile.readline())
            for row in datafile:
                data.append([float(k) for k in finder.findall(row)])
    
    print tsp(np.array(data))

if __name__ == "__main__":
    main()


