r={1:0,2:0,3:0}
#r={1:0,2:0}
for i in r:
    for j in r:
        if(i!=j):
            print("enter the value for ",j)
            r[j]=r[j]+int(input())
print("The max score is for student",max(r,key=r.get))
print(r)