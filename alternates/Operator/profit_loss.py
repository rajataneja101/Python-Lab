#03/02/2017

price_store     = input("Enter average price of the book when bought at an outlet store : ")
price_online    = input("Enter average price of the book when bought online : ") 

difference = int(price_store) - int(price_online)

if(difference < 0):
    difference = -1 * difference

print("The difference in prices between online and store bought books are : ", difference)