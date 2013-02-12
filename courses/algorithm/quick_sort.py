
def quick_sort (arr):
    def swap(l, a,b):
        temp = l[a]
        l[a] = l[b]
        l[b] = temp
        return l
    if len(arr)==0 or len(arr)==1:
        return arr
    pivot = arr[0]
    i = 1
    for j in range(i,len(arr)):
        if arr[j]<pivot:
            arr = swap(arr, i, j)
            i += 1
    arr = swap(arr, 0, i-1)
    return quick_sort(arr[:i-1])+arr[i]+quick_sort(arr[i:])
        
from math import ceil
def quick_sort_count (arr, index, median=False):
    def swap(l, a,b):
        temp = l[a]
        l[a] = l[b]
        l[b] = temp
        return l
    def find_median(x):
        candi = sorted([x[0],x[-1],x[int(ceil(len(x)/2.))]])[1]
        return swap(x, 0, x.index(candi))

    if len(arr)==0 or len(arr)==1:
        return arr, 0
    
    print arr
    if index != 0:
        arr = swap(arr, index, 0)
    if median:
        arr = find_median(arr)
        print arr
    pivot = arr[0]
    i = 1
    for j in range(i,len(arr)):
        if arr[j]<pivot:
            arr = swap(arr, i, j)
            i += 1
    arr = swap(arr, 0, i-1)
    arr[:i-1], t1 = quick_sort_count(arr[:i-1], index, median)
    arr[i:], t2 = quick_sort_count(arr[i:], index, median)
    return arr, len(arr)+t1+t2-1

def test (l):
    from random import shuffle
    x=range(l)
    x = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    #shuffle(x)
    #print "The original data set is ", x
    arr, result = quick_sort_count(x, 0, True)
    #print "The sorted data set is ", arr
    print "The overall comparison # is ", result

if __name__ == "__main__":
    test(10)





