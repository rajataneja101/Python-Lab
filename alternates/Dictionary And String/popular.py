#10/02/2017

stu={1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0}

for i in stu:
    print(" Student ", i)
    for j in stu:
        if(i != j):
            print("Enter value for : ", j)
            stu[j] = stu[j] + int(input())

print("The max score is for student : ", max(stu, key=stu.get))
print(stu)