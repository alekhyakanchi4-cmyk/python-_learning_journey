#module =python file
#predefined modules
#userdefined modules
#bultin modules
#we have to import modules
#math
import math
print(dir(math))

print(math.sqrt(70))
print(math.pi)
print(math.gcd(34,6))
print(math.factorial(5))
print(math.lcm(10,20))
print(math.floor(25.99))
print(math.cos(45))
print(math.ceil(7))
#time
import time
print(dir(time))
print(time.time())
print(time.asctime())
print(time.localtime())
#time.sleep wait for seconds how much we want
def nm():
    print("hi")
    time.sleep(5)
    print("i AM ALEKHYA")
    time.sleep(5)
    print("ds branch")
nm()
#finding time how much it take to run
s=time.time()
def nm():
    print("hi")
    time.sleep(5)
    print("i AM ALEKHYA")
    time.sleep(5)
    print("ds branch")
nm()
e=time.time()
time=e-s
print(time)


import calendar
print(dir(calendar))
print(calendar.calendar(2004))
print(calendar.month(2026,9))
print(calendar.isleap(2024))
import random
print(dir(random))
print(random.randint(1000,10000))
print(random.randrange(1,10))
print(random.sample())
import module
a=40
def mod():
    print("hi iam module1")
module.mod()
from Task import add,sub,div,mul

while True:
    print("1.add 2.sub,3.div,4.mul,5.exit")
    ch=int(input("enter choice:"))
    if ch==1:
        x=int(input())
        y=int(input())
        res=add(x,y)
        print(res)
    elif ch==2:
        x=int(input())
        y=int(input())
        res=sub(x,y)
        print(res)
    elif ch==3:
        x=int(input())
        y=int(input())
        res=div(x,y)
        print(res)
    elif ch==4:
        x=int(input())
        y=int(input())
        res=mul(x,y)
        print(res)
    else:
        exit
        




















