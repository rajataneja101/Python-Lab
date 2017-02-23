#03/02/2017

print("Zellers algorithm to return the day of the week for any year")

# Get input
month   = int(input("Month   : "))
day     = int(input("Day     : ")) # sample comment
year    = int(input("Year    : "))
cent    = int(input("Century : ")) # thsi should not be here

# Start of algorithm
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

# days map
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

print("The day is", days[Z%7])