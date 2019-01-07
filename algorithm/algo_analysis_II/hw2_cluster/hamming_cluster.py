import os
import re
from union_find import union_find

finder = re.compile("-?\d+")


def diff(a, b):
    return sum(1 for k in range(len(a)) if a[k] != b[k])


def diff_less(a, b, thres):
    count = 0
    for k in range(len(a)):
        if a[k] != b[k]:
            count += 1
            if count >= thres:
                return False
    return True


def put_point(x, already, p, threshold):
    found = False
    keys = set(already)
    while len(keys) > 0:
        i = keys.pop()
        if not found and diff_less(i, p, threshold):
            x.alldata[p] = x.alldata[i]
            keys.difference(set(x.cluster[x.alldata[i]]))
            x.cluster[x.alldata[i]].append(p)
            found = True
        if found and diff_less(i, p, threshold):
            keys.difference(set(x.cluster[x.alldata[i]]))
            x.union(x.alldata[i], x.alldata[p])
    if not found:
        x.alldata[p] = p
        x.cluster[p] = [p]
    already.append(p)


def iterate(data):
    x = union_find()
    already = []
    [put_point(x, already, k, 3) for k in data]
    print x.length()


def main():
    temp = []
    with open(os.path.join(
        os.path.dirname(__file__), "clustering_big.txt")) as datafile:
        num_of_nodes, digits = [int(k)
                                for k in finder.findall(datafile.readline())]
        for row in datafile:
            temp.append("".join(finder.findall(row)))
    iterate(temp)


if __name__ == "__main__":
    main()
