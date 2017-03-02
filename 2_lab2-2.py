import re
str1=input("Enter string 1")
str2=input("Enter string 2")
m=re.search(str2,str1)
print(str1.count(str2))
iter = re.finditer(str2, str1)
indices = [m.start(0) for m in iter]
print(indices)