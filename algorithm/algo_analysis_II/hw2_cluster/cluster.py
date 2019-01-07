import os
import re
import numpy as np
from union_find import union_find

finder = re.compile("-?\d+")


def cluster(npar, all, target):
    x = union_find()
    count = 0
    length = len(npar)
    x.init_dataset(npar)
    while x.length() > target and count < length:
        x.put(npar[count])
        count += 1
    # calculate max-spacing and get rid of circles
    while count < length:
        if x.is_circle(npar[count, 0], npar[count, 1]):
            count += 1
        else:
            return npar[count, -1]
    return 0


def main():
    dt = [('n1', int), ('n2', int), ('cost', int)]
    temp = []
    with open(os.path.join(
        os.path.dirname(__file__), "clustering1.txt")) as datafile:
        num_of_nodes = int(datafile.readline())
        for row in datafile:
            temp.append([int(k) for k in finder.findall(row)])
    temp = np.sort(np.array([tuple(k) for k in temp], dt), order=['cost'])
    temp = np.array([list(temp[k]) for k in range(len(temp))])
    print cluster(temp, num_of_nodes, 4)


if __name__ == "__main__":
    main()
