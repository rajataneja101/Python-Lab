def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue
alist=[]
while True:
    i=input()
    if(i == 'end'):
        break
    elif(i!='end'):
        alist.append(int(i))
       # type(alist)
insertionSort(alist)
print(alist)

blist = [54,26,93,17,77,31,44,55,20]
bubbleSort(blist)
print(blist)
