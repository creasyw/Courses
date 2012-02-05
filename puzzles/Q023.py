#Problem 23:
#A perfect number is a number for which the sum of its proper divisors 
#is exactly equal to the number. For example, the sum of the proper 
#divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 
#is a perfect number.
#
#A number n is called deficient if the sum of its proper divisors is 
#less than n and it is called abundant if this sum exceeds n.
#
#As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the 
#smallest number that can be written as the sum of two abundant numbers 
#is 24. By mathematical analysis, it can be shown that all integers 
#greater than 28123 can be written as the sum of two abundant numbers. 
#However, this upper limit cannot be reduced any further by analysis 
#even though it is known that the greatest number that cannot be expressed 
#as the sum of two abundant numbers is less than this limit.
#
#Find the sum of all the positive integers which cannot be written as the 
#sum of two abundant numbers.

from math import sqrt

def findDivisor(num):
	""" find all of the divisors for a given input """
	divisors = [1]
	for i in range(2,int(sqrt(num))+1):
		if num%i==0:
			divisors.append(i)
			temp = num/i
			if temp !=i:
				divisors.append(temp)
	return divisors
	
def sumDivisor(inputList):
	""" sum up all elements within the input list """
	result = 0
	for i in inputList:
		result += i
	return result

def updateSumList(abList, sList):
	""" update the list of sum of two abundant numbers """
	for element in abList:
		# the only difference is the latest added element
		sList.add(element + abList[-1])
	return sList


result = 0
abundantList = []
sumList = set([])
for i in range(1,28123):
	if i in sumList:
		flag = True
	else:
		flag = False
	divisorList = findDivisor(i)
	if i < sumDivisor(divisorList):
		abundantList.append(i)
		sumList = updateSumList(abundantList, sumList)
	if flag:
		continue
	else:
		temp = i
	result += i
print "result = ", result
print "the last number is ",temp
