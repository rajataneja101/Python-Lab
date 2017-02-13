
def day_week(d, m, y):
    day_names = ['Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    if m < 3:
        m = m + 12
        y = y - 1
    day = (((13 * m + 3) // 5 + d + y + (y / 4) - (y // 100) + (y // 400)) % 7)
    return day_names[int(day)]

a=int(input("Enter month: "))
b=int(input("Enter day: "))
c=input("Enter year: ")
d=input("Enter century: ")
e=d+c
f=day_week(a,b,int(e))
print("It's a ",f)