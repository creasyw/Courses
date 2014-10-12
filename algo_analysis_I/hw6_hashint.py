#The goal of this problem is to implement a variant of the 2-SUM algorithm (covered in the Week 6 lecture on hash table applications).
#The file contains 500,000 positive integers (there might be some repetitions!).This is your array of integers, with the ith row of the file specifying the ith entry of the array.
#
#Your task is to compute the number of target values t in the interval [2500,4000] (inclusive) such that there are distinct numbers x,y in the input file that satisfy x+y=t. (NOTE: ensuring distinctness requires a one-line addition to the algorithm from lecture.)
#
#Write your numeric answer (an integer between 0 and 1501) in the space provided.
#
#
#OPTIONAL COMMENT: You might notice that the chosen targets are relatively small numbers. (There is a good reason for this. Can you guess what would be the problem with a similar interval of larger targets?) You are welcome to add extra optimizations that take advantage of this fact, though it is not required for the assignment.
#
#OPTIONAL CHALLENGE: If this problem is too easy for you, try implementing your own hash table for it. For example, you could compare performance under the chaining and open addressing approaches to resolving collisions.
#
#REQUEST FOR COMMENTS: Do you have a favorite hash table application that could serve as a programming assignment for this course? Post your idea to the discussion form, and maybe it will be used in the next iteration of this course!


# use hashing, use chains to deal with conflicts
def loadData():
    MAX = 0
    data = open("HashInt.txt","r").read()
    stringlist = data.split("\n")
    hashlist = [False for i in range(4000)]
    datalist = []
    for string in stringlist:
        if string == '':
            continue
        value = int(string)
        if value > 4000:
            continue
        datalist.append(value)
        hashlist[value-1]=True
    #print MAX,len(hashlist)
    return datalist,hashlist

def SUM2_hash(list,hashlist,sum):
    for item in list:
        if sum>item*2 and hashlist[sum-item-1]:
            return True,(item,sum-item)
    return False,None

def main():
    datas,hashs = loadData()
    total = 0
    invalidlist= []
    for i in range(2500,4001):
        flag,pair = SUM2_hash(datas,hashs,i)
        if flag:
            total += 1
        else:
            invalidlist.append(i)
    #print len(invalidlist)
    print total
    
main()
