#for loops
for i in range(5):
    print(i)   
for i in range(1,10,2):
    print(i)
#even numbers
for i in range(0,20,2):
    if i%2==0:
        print(i)
#odd numbers
for i in range(1,20,2):
    if i%2!=0:
        print(i,end=',')
#sum
for i in range(5):
    a=int(input())
    b=int(input())
    print(a+b)
#count
x=int(input())
y=int(input())
c=0
for i in range(x,y):
    if i%2==0:
        c=c+1
print(c)
#1-10 numbers
for i in range(1,11):
    print(i)

#from 1 to n
n=int(input())
for i in range(1,n+1):
    print(i)
    
#sum of n natural numbers
n=int(input())
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)



