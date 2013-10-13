import os, re
import numpy as np
import random
from math import log

finder = re.compile("-?\d+")

def sat(clause, num):
    for i in range(int(log(num, 2))):
        # random initial assignment
        # using length num+1 so that the index in clause can be directly mapping to
        var = [False]+[bool(random.getrandbits(1)) for k in range(num)]
        for j in range(2*num**2):
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

    print sat(clause, num)

if __name__ == "__main__":
    main()


