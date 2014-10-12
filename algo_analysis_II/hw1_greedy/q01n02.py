import os, re
import numpy as np
finder = re.compile("\d+")

def q1(v, dt):
    data = np.array([(k[0],k[1],k[0]-k[1]) for k in v], dtype = dt)
    data = np.sort(data, order=['diff', 'weight'])[::-1]
    return weighted_completion(np.array([list(k) for k in data]))

def q2(v, dt):
    data = np.array([(k[0],k[1],float(k[0])/k[1]) for k in v], dtype = dt)
    data = np.sort(data, order=['diff', 'weight'])[::-1]
    return weighted_completion(np.array([list(k) for k in data]))

def weighted_completion(lst):
    lst[0,2] = lst[0,1]
    for i in range(1, len(lst)):
        lst[i,2] = lst[i-1,2]+lst[i,1]
    return int(sum(lst[:,0]*lst[:,2]))
        

def main():
    dt = [('weight', int), ('length', int), ('diff', float)]
    values = []
    with open(os.path.join(os.path.dirname(__file__), "jobs.txt")) as datafile:
        datafile.readline()
        for row in datafile:
            values.append([int(k) for k in finder.findall(row)])
    print q1(values, dt)
    print q2(values, dt)


if __name__ == "__main__":
    main()
            




