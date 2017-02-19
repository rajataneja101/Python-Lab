import re

#print(re.split(r'(s*)','here are some words'))

#print(re.split(r'[a-fA-F]','djsdssAGJJHSIW'))
#print(re.match(r'[^\d]\w*\@\w+[.]+\w+','rajat101@gmai.l.com').group())
print(re.findall(r'[^\d]\w+\@\w+\.+\w+','123rajat101@gmail.com'))
print(re.match(r'[^\d]\w*\@\S+','rajat101@gmai.l.com').group())