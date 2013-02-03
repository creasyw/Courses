# Another example for "Divide and Conqure".
# The algorithm is much like the merge_sort without a tricky part that 
# the lexical scope in closure needs to get passed by mutable datatype.


def inversion_array (arr):
    count = [0]
    def count_split (x, y):
        if x== []:
            return y
        elif y == []:
            return x
        else:
            acc = []
            ly = len(y)
            l = len(x)+ly
            for k in range(l):
                if x == []:
                    acc += y
                    break
                elif y == []:
                    acc += x
                    break
                elif x[0]<=y[0]:
                    acc.append(x.pop(0))
                else:
                    count[0] += len(x)
                    acc.append(y.pop(0))
            return acc

    def sort_count (x):
        if len(x) == 1:
            return x
        else:
            half = len(x)/2
            x1 = sort_count(x[:half])
            x2 = sort_count(x[half:])
            return count_split(x1, x2)
    sort_count(arr)
    return count[0]

def test (l):
    from random import shuffle
    x=range(l)
    shuffle(x)
    print "The original data set is ", x
    print "The inversions # is ", inversion_array(x)

if __name__ == "__main__":
    test(10)



