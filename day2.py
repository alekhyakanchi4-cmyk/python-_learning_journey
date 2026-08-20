#operators
#floor division returns quotient
#if it is negative numbers it rounds to less than number 
print(5//2)
print(-5//2)
print(5/2)


print(20//6)
print(-20//6)
print(20//-6)
print(-20//-6)

print(20.5//6)
#modulus which returns remainder
print(-5%2)
print(-10%2)

print(-15%2)
print(-19/4)
print(-4%19)
print(-8%2)
print(-15%4)

print(-20%6)
print(20%6)
print(-20%-6)
print(20%-6)

print(6%20)
print(-6%20)
print(6%-20)
print(-6%-20)
print(2%5)
#exponentiation
base=2
exp=3
result=base**exp
print(result)

base=int(input())
exp=int(input())
result=base**exp
print(result)

base=int(input())
exp=int(input())
result=pow(base,exp)
print(result)

#to  extract digits from a 3 or 4 or anyother number we use // and %

a=527
seconddigit=(a//10)%10
print(seconddigit)

#3rd digit
b=2989
res=(b//100)%10
print(res)

#last digit
n=290
print(n%10)
#relational operators
print(12<=14)
print(515>900)
print(12>=12)
print(12==12)
print(13==11)
print(15!=45)
print(16!=16)
#and return true if both conditions are true
res=19>23 and 23>32
print(res)
#or return if any one condition is true all are true
print(3 or 10>9 )
print(10<5 or 0 or 0)
print(10<5 or 1 or 10<5)
print(10<5 or 0 or 10<5)
#not negates the value of expresion
k=11
s= not k
print(s)
print(k)
r=12>30
s=not r
print(s)
print(r)

r=12<30
s=not r
print(s)
print(r)

print('a' in "alekhya")
print('a' not in "alekhya")
#is checks whether address same or not
k=22
print(id(k))
v=22
print(id(v))
print(k is v)
s=221
print(id(s))
print(k is s)
print(k is not s)
print(k is not v)

#years months days
a=int(input())
b=(a//365)
c=a%365
d=c//30
e=c%30
print(a)
print(b)
print(d)
print(e)

#days hours min
a=int(input())
days=a//(24*60)
rms=a%(24*60)
hours=rms//60
mins=rms%60
print(days,hours,mins)


a=int(input())
days=a//(24*60)
rms=a%(24*60)
hours=rms//60
mins=rms%60
print(f"no of days {days} no of hours{hours} no of min{mins}")

#sum of reverse and actual value 
a=int(input())#2digit#23
c=a//10         #2
d=a%10          #3
re=d*10+c       #3*10+2=32
sum=a+re        #23+32
print(sum)      #55


#seconds to hours,minutes,sec
seconds=int(input())
hours=seconds//3600
minutes=(seconds%3600)//60
seconds=seconds%60
print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
print("%02d:%02d:%02d" %(hours,minutes,seconds))



