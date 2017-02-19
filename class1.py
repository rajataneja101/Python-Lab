q=input("Input the code file")
mod=__import__(q)
i=input("Enter the file with input values")
e=input("Enter the file with evaluation value")
o=input("Enter the file where you want to store the values")
sm=mod.fun(i)
print(sm)
p=open(o,'w')
p.write(str(sm))
p.close()
q=open(e,'r')
p=open(o,'r')
n=p.read()
m=q.read()
if(n==m):
    print("100%")
else:
    print("0%")



    