#addition
a=float(input())
b=float(input())
c=a+b
print(c)

#area of rectangle
l=int(input())
b=int(input())
area=l*b
print("area:",area)

#area of rectangle
l=float(input())
b=float(input())
area=l*b
print("area:",area)

#simple intrest
price=float(input())
time=float(input())
rate=float(input())
si=(price*time*rate)/100
print("si:",si)


#swaping
a=int(input())
b=int(input())
temp=a
a=b
b=temp
print(a,b)

#swaping
a=int(input())
b=int(input())
print("before swaping")
print(a,b)
a,b=b,a
print("after swaping")
print(a,b)

#calculating total amount including gst
obill=float(input())
gst=float(input())
totalgst=(obill*gst)/100
totalamount=obill+totalgst
print("totalgst:",totalgst)#gst calculation
print(totalamount)
