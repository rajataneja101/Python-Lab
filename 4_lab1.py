import re
d=0
e=open("file1.txt",'r')
q=open("file2.txt",'w')
for a in e.readlines():
    if(re.match(r'#\w*#',a)):
        d+=1
    else:
        q.writelines(a)
e.close()
q.close()
q=open("file2.txt",'r')
for a in q.readlines():
    print(a)
q.close()