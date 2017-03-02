#03/02/2017

amount      = int(input("Enter the total amount : "))
vat_percent = int(input("Enter VAT percentage : "))

vat_amount = amount * vat_percent//100
net_amount = amount + vat_amount

print("VAT Amount : ", vat_amount)
print("Net Amount : ", net_amount)