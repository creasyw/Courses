#Problem 21:
#Let d(n) be defined as the sum of proper divisors of n (numbers  
#less than n which divide evenly into n). If d(a) = b and d(b) = a,  
#where a != b, then a and b are an amicable pair and each of a and b  
#are called amicable numbers. 
# 
#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20,  
#22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of  
#284 are 1, 2, 4, 71 and 142; so d(284) = 220. 
# 
#Evaluate the sum of all the amicable numbers under 10000. 


def findDivisor(num):
	""" find all of the divisors for a given input """
	divisors = [1]
	for i in range(2,num/2-1,1):
		if num%i==0 and not (i in divisors):
			divisors.append(i)
			divisors.append(num/i)
	return divisors
	
def sumDivisor(inputList):
	""" sum up all elements within the input list """
	result = 0
	for i in inputList:
		result += i
	return result

amicableList = []

#dList = findDivisor(220)
#dSum = sumDivisor(dList)
#print "The sum is ", dSum
# finding all elements in the required range
for i in range(3,10000):
	if i in amicableList:
		continue
	divisorList = findDivisor(i)
	divisorSum = sumDivisor(divisorList)
	if i >= divisorSum:
		continue
	counterpart = divisorSum
	divisorList = findDivisor(counterpart)
	divisorSum = sumDivisor(divisorList)
	if i != divisorSum:
		continue
	else:
		amicableList.append(i)
		amicableList.append(counterpart)
		print " find two numbers %d and %d" % (i, counterpart)
	
# sum up all acceptable elements
result = 0
for i in amicableList:
	result += i

print "The final result is ", result
