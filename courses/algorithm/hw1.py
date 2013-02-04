from inversion_array import inversion_array
import os

def main ():
    arr = []
    with open(os.path.join(os.path.dirname(__file__), "IntegerArray.txt")) as datafile:
        for row in datafile:
            arr.append(int(row))
    print inversion_array(arr)

if __name__=="__main__":
    main()


