# Write function to compute Nth fibonacci number
def fib (n):
    return fib(n-1)+fib(n-2) if n>1 else n
def test_fib (n):
    result = []
    for i in range(n):
        result.append(fib(i))
    print "The first %sth fibonacci numbers are:"%(n)
    print result

# Print out the grade-school multiplication table up to 12x12
import sys
def multi_table (n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            sys.stdout.write("%d\t"%(i*j))
        sys.stdout.write("\n")

# Write a function that sums up integers from a text file, one int per line.
import re
def sumFile (filename):
    try:
        f = open(filename, 'r')
    except:
        print "The given file cannot be opened!!"
        return
    finder = re.compile("\d+")
    result = 0
    for line in f:
        # only add the first integer appear in each line
        result += int(finder.findall(line)[0])
    print "The sum of the file is ", result

# Write function to print the odd numbers from 1 to 99.
def print_odds ():
    for i in range(1, 100, 2):
        sys.stdout.write("%d\t"%(i))

