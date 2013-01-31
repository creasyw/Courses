def merge_sort (x):
    def merge(x, y, acc):
        if x== []:
            return acc+y
        elif y == []:
            return acc+x
        else:
            if x[0]<=y[0]:
                acc.append(x.pop(0))
            else:
                acc.append(y.pop(0))
            return merge(x, y, acc)
    


def test (l):
    from random import shuffle
    x=range(l)
    shuffle(x)
    print "The original data set is ", x
    print "The sorted data set is ", merge_sort(x)

if __name__ == "__main__":
    test(100)


