#03/02/2017

n=int(input())
for i in range(0,n):
    for k in range(0,i):
        print("\\ \\ ",end="")
    for j in range(i*2,(n*2-1)):
        print("! ! ", end="")
    for k in range(0, i):
        print("/ / ", end="")
    print("\n")