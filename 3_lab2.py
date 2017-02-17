class polygon:
    no_of_side=0
    sides=[]
    def __init__(self,no_of_side):
        self.no_of_side=no_of_side
    def input_sides(self):
        for i in range(0,self.no_of_side):
            print("Enter side ",i+1)
            n=int(input())
            self.sides.append(n)
    def print_sides(self):
        for i in range(0, self.no_of_side):
            print("The side ",(i+1),self.sides[i])
class triangle(polygon):
    def __init__(self):
        self.no_of_side=3
    def find_area(self):
        sum=0
        for i in range(0, self.no_of_side):
            sum+=self.sides[i]
        return (sum/2)
n=int(input("Enter the no. of sides"))
#p=polygon(n)
q=triangle()
if n==3:
    q.input_sides()
    q.print_sides()
    k=q.find_area()
    print(k)
else:
    p=polygon(n)
    p.input_sides()
    p.print_sides()
    print

