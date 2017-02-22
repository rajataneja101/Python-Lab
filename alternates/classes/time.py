#16/2/2017

import copy

class time:
    hours=0
    minutes=0
    seconds=0

    def __init__(self,hours=0,minutes=0,seconds=0):
        self.hours      =   hours
        self.minutes    =   minutes
        self.seconds    =   seconds
    
    def input_values(self):
        print("Enter time (hh:mm:ss) : ")
        
        self.hours      = int(input("Enter hours : "))
        self.minutes    = int(input("Enter Minutes : "))
        self.seconds    = int(input("Enter seconds : "))
    
    def print_values(self):
        print(self.hours, ':', self.minutes, ':', self.seconds)

    def __add__(self, other):
        self.hours      = self.hours + other.hours
        if(self.hours >= 24):
            self.hours -= 24
        self.minutes    = self.minutes + other.minutes
        if(self.minutes >= 60):
            self.minutes -= 60
            self.hours += 1
        self.seconds    = self.seconds + other.seconds
        if(self.seconds >= 60):
            self.seconds -= 60
            self.minutes += 1
        return time(self.hours, self.minutes, self.seconds)

    def __sub__(self, other,t3):
        t3.hours    = t3.hours - other.hours
        if(t3.hours < 24):
            t3.hours += 24
        t3.minutes  = t3.minutes - other.minutes
        if(t3.minutes < 0):
            t3.minutes += 60
            t3.hours -= 1
        t3.seconds  = t3.seconds - other.seconds
        if(t3.seconds < 0):
            t3.seconds += 60
            t3.minutes -= 1
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

print("t1+t2",time.__add__(t1,t2))
print("t1-t2=",time.__sub__(t1,t2,t3))