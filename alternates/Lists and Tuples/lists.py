#03/02/2017

print("Enter list elements (type 'end' to stop)")

temp = ""
user_list = []

#start of loop
while(temp != "end"):
    temp = input()
    if(temp != "end"):
        user_list.append(int(temp))
#end of loop

print("Your list is :: ", user_list)

user_list.sort()

print("After sorting :: ", user_list)