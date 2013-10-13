import os, re
import numpy as np
import random

finder = re.compile("-?\d+")


def main():
    import sys
    assert len(sys.argv)==2, "The proper input format is: ~$ python SCRIPT.py data_file start_node"
    filename = sys.argv[1]
    with open(os.path.join(os.path.dirname(__file__), filename)) as datafile:
            num = int(datafile.readline())
            clause = np.zeros((num, 2))
            count = 0
            for row in datafile:
                 clause[count] = [int(k) for k in finder.findall(row)]
                 count += 1
    # pre-processing
    # using length num+1 so that the index in clause can be directly mapping to
    var = [bool(random.getrandbits(1)) for k in range(num+1)]
    print clause
    print var

if __name__ == "__main__":
    main()


