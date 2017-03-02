# 17/02/2017

import re

ref_string = input("Enter reference string : ")
search_string = input("Enter search string : ")

index = ref_string.find(search_string)

if(index !=-1):
    print("Number of occurances : ", ref_string.count(search_string))
    for m in re.finditer(search_string, ref_string):
        print(m.span())