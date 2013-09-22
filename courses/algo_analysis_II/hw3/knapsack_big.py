import os
import re
import numpy as np

finder = re.compile("-?\d+")

def knapsack(arr, weight, size):
    print weight
    print size
    previous = np.zeros(weight+1)
    for k in range(arr[0,1],weight+1):
        previous[k] = arr[0,0]
    for i in range(1, size):
        current = np.zeros(weight+1)
        for j in range(weight+1):
            if j-arr[i,1] >=0:
                current[j] = max(previous[j], previous[j-arr[i,1]]+arr[i,0] )
            else:
                current[j] = previous[j]
        previous = current
    return current[-1]

def main():
    temp = []
    with open(os.path.join(os.path.dirname(__file__), "knapsack_big.txt")) as datafile:
            weight, size = [int(k) for k in finder.findall(datafile.readline())]
            for row in datafile:
                temp.append([int(k) for k in finder.findall(row)])
    temp = np.array(temp)
    print knapsack(temp, weight, size)

if __name__ == "__main__":
    main()

#4243395
