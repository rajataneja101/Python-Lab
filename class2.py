def fun(i):
    sum=0
    k = open(i, 'r')
    for i in k.readlines():
        sum+=int(i)
    k.close()
    return sum