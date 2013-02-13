import os
from quick_sort import quick_sort_count

def run_quicksort (arr, index, median):
    _,result = quick_sort_count(arr, index, median)
    print result


def main ():
    arr = []
    with open(os.path.join(os.path.dirname(__file__), "QuickSort.txt")) as datafile:
        for row in datafile:
            arr.append(int(row))
    # Because the quick_sort is in-place sorting,
    # arr should be duplicated for different pivot choices
    arr2 = list(arr)
    arr3 = list(arr)
    _,result = quick_sort_count(arr, 0)
    print "Assign the 1st element as pivot:", result
    _,result = quick_sort_count(arr2, -1)
    print "Assign the last element as pivot:", result
    _,result = quick_sort_count(arr3, 0, True)
    print "Assign the 'median' element as pivot:", result


if __name__=="__main__":
    main()

