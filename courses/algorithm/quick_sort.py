
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
    return quick_sort(arr[:i])+quick_sort(arr[i:])


def test (l):
    from random import shuffle
    x=range(l)
    shuffle(x)
    print "The original data set is ", x
    print "The sorted data set is ", quick_sort(x)

if __name__ == "__main__":
    test(20)





