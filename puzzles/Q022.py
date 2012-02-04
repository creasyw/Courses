#Problem 22:
#Using names.txt (http://projecteuler.net/project/names.txt), 
#a 46K text file containing over five-thousand first names, begin by 
#sorting it into alphabetical order. Then working out the alphabetical 
#value for each name, multiply this value by its alphabetical position 
#in the list to obtain a name score.
#
#For example, when the list is sorted into alphabetical order, COLIN, 
#which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the 
#list. So, COLIN would obtain a score of 938 * 53 = 49714.
#
#What is the total of all the name scores in the file?


from sys import argv
import string

def valueOfWord(word, index):
	""" calculate the value of single word """
	value = 0
	word = word.lower()
	for ch in word:
		if ch =="\"":
			continue
		#print "the character is %s" % ch
		value += string.lowercase.index(ch) +1
	return value*index

script, inputFile = argv

input = open(inputFile)
indata = input.read()
wordList = indata.split(',')
wordList.sort()

result = 0
count = 1
for element in wordList:
	result += valueOfWord(element, count)
	count +=1
print "the final sum is ", result

input.close()

