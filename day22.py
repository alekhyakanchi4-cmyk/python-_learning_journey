#OUTSIDE THE FUNCTION GLOBAL DATA
#inside the functions local data

positional arguements
keyword
default
variable length

#variable length keyword arguements
def one(**kwargs):
    print(kwargs)
one(name="balu",vlg="tiruvuru",age=23)

def one(**s):
    for i in s.items():
        
        print(i)
one(name="balu",vlg="tiruvuru",age=23)


#arm strong 
num=int(input())
temp=num
num_digits=len(str(num))
digit_sum=0
while temp>0:
    digit=temp%10
    digit_sum+=digit**num_digits
    temp=temp//10
if num==digit_sum:
    print("armstrong")
else:
    print("not")
    
#by using functions


def armstrong(x):
    num=x
    temp=num
    num_digits=len(str(num))
    digit_sum=0
    while temp>0:
        digit=temp%10
        digit_sum+=digit**num_digits
        temp=temp//10
    if num==digit_sum:
        print("armstrong")
    else:
        print("not")
s=int(input())
armstrong(s)
#perfect number

num=int(input())
sum=0
for i in range(1,num):
    if num%i==0:
        sum=sum+i
if num==sum:
    print("perfect number")
else:
    print("not")
#by using function
def perfect(x):
    num=x
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum=sum+i
    if num==sum:
        print("perfect number")
    else:
        print("not")
s=int(input())
perfect(s)
    
#stack heap memory


def one():
    print(l+s)
l=[10,20,30,40,50]
s=["b","a","b","y","b"]
one()



def one(x,y):
    print(l+s)
l=[10,20,30,40,50]
s=["b","a","b","y","b"]
one(l,s)

def one(x,y):
   return x+y
l=[10,20,30,40,50]
s=["b","a","b","y","b"]
x=one(l,s)
print(x)


#sum
def one(x):
    s=0
    for i in x:
        s=s+i
    print(s)
l=[10,20,30,40,50]
one(l)


#passing function as input another function
def add(x):
    return x+10
def out(y):
    print(y)
out(add(10))


#square passing function as input another function
def sq(x):
    return x**2
def out(y):
    print(y)
out(sq(13))





    
        
