import math
p=int(input("Enter side1: "))
q=int(input("Enter side2: "))
r=int(input("Enter the angle(in degress): "))
s=math.sqrt(p*p+q*q-2*p*q*math.cos(math.radians(r)))
print("The third side is:",s)
