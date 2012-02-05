# Problem 24
# A permutation is an ordered arrangement of objects. For example, 
# 3124 is one possible permutation of the digits 1, 2, 3 and 4. If 
# all of the permutations are listed numerically or alphabetically, 
# we call it lexicographic order. The lexicographic permutations of 
# 0, 1 and 2 are:	012   021   102   120   201   210
# 
# What is the millionth lexicographic permutation of the digits 0, 
# 1, 2, 3, 4, 5, 6, 7, 8 and 9? (10!=3,628,800)

# SOLUTION: A  B  C  D  E  F  G  H  I  J
# Possi     9! 8! 7! 6! 5! 4! 3! 2! 1! 0!
# Index     0  1  2  3  4  5  6  7  8  9
#              0  1  2  3  4  5  6  7  8
#                 ......

import math

target = 1000000
result = 0
count = 9	# the outerest round is x*10^9
numList = []

for i in range (0,count+1):
	numList.append(i)

leftValue = target-1
while count>1 :
	temp = math.factorial(count)
	index = leftValue/temp
	result += numList.pop(index)*math.pow(10,count)
	leftValue = leftValue%temp
	count = count-1

result += numList.pop(leftValue)*10
result += numList.pop(0)

print "The %dth of the premutation is %d" % (target,result)

