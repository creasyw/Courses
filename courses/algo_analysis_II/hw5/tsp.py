import os, re
import numpy as np

finder = re.compile("-?\d+\.?\d*")

def gen_name(lst):
    return reduce(lambda i, j: i+str(j), sorted(lst), '')




def main():
    import sys
    assert len(sys.argv)==2, "The proper input format is: ~$ python SCRIPT.py data_file start_node"
    filename = sys.argv[1]
    data = []
    with open(os.path.join(os.path.dirname(__file__), filename)) as datafile:
            num = int(datafile.readline())
            for row in datafile:
                data.append([float(k) for k in finder.findall(row)])
    
    print np.array(data)

if __name__ == "__main__":
    main()


