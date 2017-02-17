s=input("Enter a string")
w=input("Enter a sub string")
index=0
while index < len(s):
    index = s.find(w, index)
    if index == -1:
        break
    print('found at', index)
    index += 2