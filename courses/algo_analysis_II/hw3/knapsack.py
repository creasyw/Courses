import os
import re
import numpy as np

finder = re.compile("-?\d+")

def knapsack(arr, weight, size):
    assert size == len(arr), "ERROR: The size is not equal to input array!!"
    result = np.zeros((size, weight+1))
    for k in range(arr[0,1],weight+1):
        result[0,k] = arr[0,0]
    for i in range(1, size):
        for j in range(weight+1):
            if j-arr[i,1] >=0:
                result[i,j] = max( result[i-1, j], result[i-1, j-arr[i,1]]+arr[i,0] )
            else:
                result[i,j] = result[i-1, j]
    return result

def reverse_find_route(arr, result):
    point = len(result[0])-1
    route = []
    for i in range(len(result)-1, 1, -1):
        if result[i][point] != result[i-1][point]:
            route.append(i+1)
            point -= arr[i,1]
    return route[::-1]

def main():
    import sys
    assert len(sys.argv)==2, "The proper input format is: ~$ python SCRIPT.py data_file"
    filename = sys.argv[1]
    temp = []
    with open(os.path.join(os.path.dirname(__file__), filename)) as datafile:
            weight, size = [int(k) for k in finder.findall(datafile.readline())]
            for row in datafile:
                temp.append([int(k) for k in finder.findall(row)])
    temp = np.array(temp)
    optimal_value = knapsack(temp, weight, size)
    items = reverse_find_route(temp, optimal_value)
    print "The optimal value is: ", int(optimal_value[-1, -1])
    print "The items are: ", items

if __name__ == "__main__":
    main()

#2493893
