import copy


class time:
    hours=00
    minutes=00
    seconds=00
    def __init__(self,hours=0,minutes=0,seconds=0):
        self.hours=hours
        self.minutes=minutes
        self.seconds=seconds
    def input_values(self):
        self.hours=int(input("Enter hours"))
        self.minutes = int(input("Enter Minutes"))
        self.seconds = int(input("Enter seconds"))
    def print_values(self):
        print(self.hours,':',self.minutes,':',self.seconds)

    def __add__(self, other):
        self.hours=self.hours+other.hours
        self.minutes = self.minutes + other.minutes
        self.seconds = self.seconds + other.seconds
        return time(self.hours, self.minutes, self.seconds)

    def __sub__(self, other,t3):
        t3.hours = t3.hours - other.hours
        t3.minutes = t3.minutes - other.minutes
        t3.seconds = t3.seconds - other.seconds
        return time(t3.hours, t3.minutes, t3.seconds)

    def __str__(self):
        return "{0}:{1}:{2}".format(self.hours,self.minutes,self.seconds)

t1=time()
t2=time()
t1.input_values()
t1.print_values()
t2.input_values()
t2.print_values()
t3=copy.copy(t1)

print("t1+t2",t1+t2)
print("t1-t2=",time.__sub__(t1,t2,t3))