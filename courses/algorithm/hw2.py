import os
from quick_sort import quick_sort_count
#import sys
#sys.setrecursionlimit(100000)


def main ():
    arr = []
    with open(os.path.join(os.path.dirname(__file__), "QuickSort.txt")) as datafile:
        for row in datafile:
            arr.append(int(row))
    _,result = quick_sort_count(arr, 0, True)
    print result
#    _,result2 = quick_sort_count(arr2, -1)
#    _,result3 = quick_sort_count(arr3, 0, True)
#    print result1, result2, result3

if __name__=="__main__":
    main()

