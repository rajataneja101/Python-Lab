
def tuple_sort(myList):
    temp = ()
    for i in range(len(myList)):
        for j in range(len(myList) - i - 1):
            if(myList[j][1] > myList[j+1][1]):
                temp = myList[j]
                myList[j] = myList[j+1]
                myList[j+1] = temp
    return myList

myTuple = ()
myList = []
check = 1

while check == 1:
    print("Enter Tuple (Separate with ',')")
    myTuple = [int(x) for x in input().split(",")]
    myList.append(myTuple)
    check = int(input("Continue? (1)"))

print("List : " , myList) 

myList = tuple_sort(myList)
print("On sorting : " , myList)