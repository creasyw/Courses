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
