import os, re
import numpy as np
import random
from math import log

finder = re.compile("-?\d+")

def preprocess(clause, num):
    new_clause = np.zeros((num+1,2), dtype=int)
    count = 0
    for item in clause:
        # connect two existing clauses
        benchmark = abs(new_clause)
        if abs(item[0]) in benchmark and abs(item[1]) in benchmark:
            # find the column # of the mathched item
            l1 = np.where(benchmark==abs(item[0]))[0][0]
            l2 = np.where(benchmark==abs(item[1]))[0][0]
            c1 = list(new_clause[l1])
            c2 = list(new_clause[l2])
            if item[0] in c1:
                c1.remove(item[0])
                e1 = c1[0]
            else:
                c1.remove(-item[0])
                e1 = -1*c1[0]
            if item[1] in c2:
                c2.remove(item[1])
                e2 = c2[0]
            else:
                c2.remove(-item[1])
                e2 = -1*c2[0]
            new_clause[count] = [e1,e2]
            new_clause[l1] = new_clause[l2] = [0,0]
        # only one of the items in the existing clauses
        elif abs(item[0]) in benchmark:
            l1 = np.where(benchmark==abs(item[0]))[0][0]
            c1 = list(new_clause[l1])
            if item[0] in c1:
                c1.remove(item[0])
                e1 = c1[0]
            else:
                c1.remove(-item[0])
                e1 = -1*c1[0]
            new_clause[count] = [e1,item[1]]
            new_clause[l1] = [0,0]
        elif abs(item[1]) in benchmark:
            l2 = np.where(benchmark==abs(item[1]))[0][0]
            c2 = list(new_clause[l2])
            if item[1] in c2:
                c2.remove(item[1])
                e2 = c2[0]
            else:
                c2.remove(-item[1])
                e2 = -1*c2[0]
            new_clause[count] = [item[0],e2]
            new_clause[l2] = [0,0]
        # add new clauses with new items
        else:
            new_clause[count] = item
        count += 1

    new_clause = np.array(filter(lambda x: x[0]!=0, list(new_clause)))
    new_num = len(set(k for k in new_clause.flat if k!=0))
    return np.array(new_clause), new_num



def sat(clause, num, new_num):
    for i in xrange(int(log(new_num, 2))):
        # random initial assignment
        # using length num+1 so that the index in clause can be directly mapping to
        var = [False]+[bool(random.getrandbits(1)) for k in range(num)]
        for j in xrange(2*new_num**2):
            index = []
            for item in clause:
                if item[0] > 0:
                    first = var[item[0]]
                else:
                    first = not var[abs(item[0])]
                if item[1] > 0:
                    second = var[item[1]]
                else:
                    second = not var[abs(item[1])]
                if not (first or second):
                    index.append(item)
            if len(index) == 0:
                return True
            pick = abs(index[random.randrange(len(index))][random.randint(0,1)])
            var[pick] = not var[pick]
    # After all loops there is no satisfied condition...
    return False

def main():
    import sys
    assert len(sys.argv)==2, "The proper input format is: ~$ python SCRIPT.py data_file start_node"
    filename = sys.argv[1]
    with open(os.path.join(os.path.dirname(__file__), filename)) as datafile:
            num = int(datafile.readline())
            clause = np.zeros((num+1, 2), dtype=int)
            count = 1
            for row in datafile:
                 clause[count] = [int(k) for k in finder.findall(row)]
                 count += 1

    clause, new_num =  preprocess(clause, num)
    print sat(clause, num, new_num)

if __name__ == "__main__":
    main()


