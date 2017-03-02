
print("Zellers algorithm to return the day of the week for any year")

month   = int(input("Month   : "))
day     = int(input("Day     : ")) 
year    = int(input("Year    : "))
cent    = int(input("Century : ")) 

month = month - 2

if month == 0:
    month = 12
    year = year - 1 
elif month == -1:
    month = 11
    year = year - 1

W = (13*month - 1)//5
X = year//4
Y = cent//4
Z = W + X + Y + day + year - 2*cent

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

print("The day is", days[Z%7])