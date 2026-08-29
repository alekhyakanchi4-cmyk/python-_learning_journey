#perfect square
'''num=int(input())
sum=0
for i in range(1,num):
    if num%i==0:
        sum=sum+i
if sum==num:
        print("perfect square")
else:
        print("not perfect square")'''

#using while
'''num=int(input())
sum=0
i=1
while i<num:
    if num%i==0:
        sum=sum+i
    i=i+1
if sum==num:
        print("perfect square")
else:
        print("not perfect square")'''

        

#fibonacci series
'''n=int(input())
a=0
b=1
print("f series")
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b'''

#using while
'''n=int(input())
a=0
b=1
i=1
while i<n:
    print(a,end=" ")
    a,b=b,a+b
    i=i+1'''
    
'''n=int(input())
even_count=0
odd_count=0
a=(n//1000000)%10
b=(n//100000)%10
c=(n//10000)%10
d=(n//1000)%10
e=(n//100)%10
f=(n//10)%10
g=n%10
if a%2==0:
    even_count=even_count+1
else:
    odd_count=odd_count+1
    
if b%2==0:
    even_count=even_count+1
else:
    odd_count=odd_count+1
if c%2==0:
    even_count=even_count+1
    
else:
    odd_count=odd_count+1
if d%2==0:
    even_count=even_count+1
else:
    odd_count=odd_count+1
if e%2==0:
    even_count=even_count+1
else:
    odd_count=odd_count+1
if f%2==0:
    even_count=even_count+1
else:
    odd_count=odd_count+1
if g%2==0:
    
    even_count=even_count+1
else:
    odd_count=odd_count+1
print(even_count)
print(odd_count)'''
#even odd count in 6digit number
'''n=input()
even_count=0
odd_count=0
for i in n:
    digit=int(i)
    if digit%2==0:
        even_count=even_count+1
    else:
        odd_count=odd_count+1
print("even count:",even_count)
print("odd count:",odd_count)'''
#using while
'''n=input()
even_count=0
odd_count=0
while n!=0:
    n=int(n)
    d=n%10
    if d%2==0:
        even_count=even_count+1
    else:
        odd_count=odd_count+1
    n=n//10
print("even count:",even_count)
print("odd count:",odd_count)'''
    
'''x=int(input())
y=int(input())
even_count=0
odd_count=0
for i in range(x,y):
    digit=i
    if digit%2==0:
        even_count=even_count+1
    else:
        odd_count=odd_count+1
print("even count:",even_count)
print("odd count:",odd_count)'''

#place of a digit

'''n=input()
place=1
for i in n:
    digit=int(i)
    n=n%10
    print(digit ,"place digit", digit*place)
    n=n//10'''
    
#nested loops
'''for i in range(4):
    for j in range(4):
        print("*",end=" ")
    print()'''
#stars from 1 to 4
'''for i in range(1,5):
    for k in range(i):
        print("*",end=" ")
    print()'''
#or
'''for i in range(4):
    for k in range(i+1):
        print("*",end=" ")
    print()'''
#stars from 6 to 1
'''for i in range(6,0,-1):
    for k in range(i):
        print("*",end=" ")
    print()'''       
#stars from 1 to 6 skip by 2        
'''for i in range(1,6,2):
    for k in range(i):
        print("*",end=" ")
    print()'''
    
'''for i in range(5):
    for k in range(i-1):
        print("*",end=" ")
    print()'''

for i in range(1,
