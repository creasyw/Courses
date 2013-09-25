import os
import re
import numpy as np

finder = re.compile("-?\d+")

def knapsack(arr, weight, size):
    data = np.zeros((2, weight+1))
    count = 1
    for k in range(arr[0,1],weight+1):
        data[0,k] = arr[0,0]
    for i in range(1, size):
        for j in range(weight+1):
            previous = count ^ 1
            if j-arr[i,1] >=0:
                data[count, j] = max(data[previous, j], data[previous, j-arr[i,1]]+arr[i,0] )
            else:
                data[count, j] = data[previous, j]
        count = previous
    return int(data[count ^ 1, -1])

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
