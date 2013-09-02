from random import randint, shuffle

def rselect (a, index):
    """Randomized selection with O(N)"""
    if len(a)==1:
        return a[0]
    pivot_index=randint(0,len(a)-1)
    pivot=a[pivot_index]
    result = [pivot]
    for i in a:
        if i >pivot:
            result.append(i)
        elif i==pivot:
            continue
        else:
            result.insert(0, i)
    new_index = result.index(pivot)
    if new_index == index:
        return pivot
    elif new_index > index:
        return rselect(result[:new_index], index)
    else:
        # index is one less than the subtracted elements
        return rselect(result[new_index+1:], index-new_index-1)

def dselect(a, index):
    """Deterministic selection without randomization but achieve
    the same complexity"""
    step = 5
    if len(a)<=2*step:
        return sorted(a)[index]
    middle = []
    for i in range(len(a)/step):
        middle.append(a[i])
    pivot = dselect(middle, index/(2*step))
    # The following is basically a copy-and-paste from rselect
    result = [pivot]
    for i in a:
        if i >pivot:
            result.append(i)
        elif i==pivot:
            continue
        else:
            result.insert(0, i)
    new_index = result.index(pivot)
    if new_index == index:
        return pivot
    elif new_index > index:
        return dselect(result[:new_index], index)
    else:
        # index is one less than the subtracted elements
        return dselect(result[new_index+1:], index-new_index-1)
    

def test (l, order):
    x=range(1, l+1)
    shuffle(x)
    print "The original data set is ", x
    # change order to index (from 0 to order-1)
    print "The selected data is ", dselect(x, order-1)

if __name__ == "__main__":
    test(100, 25)
