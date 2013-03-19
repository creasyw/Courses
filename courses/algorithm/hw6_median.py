import numpy as np
arrayseq = []
medianseq = []
for number in open("Median.txt").read().strip().split("\n"):
    arrayseq = arrayseq + [int(number)]
    if len(arrayseq) % 2 == 1:
        medianseq = medianseq + [np.median(arrayseq)]
    else:
        medianseq = medianseq + [np.median(arrayseq + [-1])]
        

print sum(medianseq)%10000
