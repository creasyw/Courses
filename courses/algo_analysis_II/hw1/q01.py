import os, re
import numpy as np
finder = re.compile("\d+")

def q1(data):
    data = np.sort(data, order=['diff', 'weight'])[::-1]
    print weighted_completion(np.array([list(k) for k in data]))

def weighted_completion(lst):
    lst[0,2] = lst[0,1]
    for i in range(1, len(lst)):
        lst[i,2] = lst[i-1,2]+lst[i,1]
    return sum(lst[:,0]*lst[:,2])
        

def main():
    dt = [('weight', int), ('length', int), ('diff', int)]
    values = []
    with open(os.path.join(os.path.dirname(__file__), "jobs.txt")) as datafile:
        datafile.readline()
        for row in datafile:
            temp = [int(k) for k in finder.findall(row)]
            values.append((temp[0], temp[1], temp[0]-temp[1]))
    q1(np.array(values, dtype=dt))


if __name__ == "__main__":
    main()
            




