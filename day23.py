def fun(n):
    if n==1000:     #base condition
        return
    print(n)
    n=n+1
    fun(n)  #recursive call
fun(1)

#recursion
def fun(n):
    if n==0:
        return
    print(n)
    fun(n-1)
fun(10)

#digits from 1 to 10
def fun(n):
    if n==0:
        return
    
    fun(n-1)
    print(n)
fun(10)

#digits from 1 to 5
def fun(n):
    if n==0:
        return
    
    fun(n-1)
    print(n)
fun(5)

#printing digits as user needs
def fun(n):
    if n==0:
        return
    
    fun(n-1)
    print(n)
s=int(input())
fun(s)
#factorial using functions
def fun(s):

    fact=1
    for i in range(1,s+1):
        fact=fact*i
    print(fact)
s=int(input())
fun(s)

#factorial using recursion 

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
s=int(input())
x=fact(s)
print(x)

#sum
def sum(n):
    if n==0:
        return n
    return n+sum(n-1)
s=int(input())
x=sum(s)
print(x)

#fabbonicci series

def fab(n):
    if n<=1:
        return n
    return fab(n-1)+fab(n-2)

s=int(input())
for i in range(s):
    print(fab(i),end=" ")



s=['1','2','3']
x=list(map(int,s))
print(x)
print(type(x))

s=list(input().split())
print(s)

print(type(s))

s=map(int,input().split())
print(s)
#int
s=list(map(int,input().split()))
print(s)

#float
s=list(map(float,input().split()))
print(s)

#square
s=[1,2,3,4,5]
def sqrt(x):
    return x*x
d=list(map(sqrt,s))
print(d)
#cube
s=[1,2,3,4,5]
def sqrt(x):
    return x*x*x
d=list(map(sqrt,s))
print(d)
#even
s=[1,2,3,4,5]
def sqrt(x):
    if x%2==0:
        return "even"
    else:
        return "odd"
d=list(map(sqrt,s))
print(d)

from functools import reduce
s=[1,2,3,4,5,6,7,8,9]
def even(x):
    if x%2==0:
        return x
d=list(reduce(even,s))
print(d)
