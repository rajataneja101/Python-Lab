p=int(input("Enter the gross amount of purchase: "))
q=int(input("Enter the VAT percentage: "))
print("VAT amount is",(p/q))
print("The computed net amount is: ",(p+(p/q)))