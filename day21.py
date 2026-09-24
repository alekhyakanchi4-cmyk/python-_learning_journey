s="banana"
countb=0
counta=0
countn=0
for i in s:
    if i=="b":
        countb+=1
    if i=="a":
        counta+=1
    if i=="n":
        countn+=1
print("'b':",countb,end=",")
print("'a':",counta,end=",")
print("'n':",countn)

#count of alphabets
s=input()
d={}
for i in s:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
print(d)

user1=input()
pasw1=int(input())
user2=input()
pasw2=int(input())
user3=input()
pasw3=int(input())
a=input('enter username:')
b=int(input("enter pass"))
if a==user1 or user2 or user3:
    if b==pasw1 or pasw2 or pasw3:
        print("found")
else:
    print("not found")

#pass and user match
d={}
for i in range(3):
    usr=input()
    pas=int(input())
    d[usr]=pas
lg_usr=input()
lg_pas1=int(input())
if lg_usr in d:
    if d[lg_usr]==lg_pas1:
        print("match")
    else:
        print("not match")
else:
    print("not match")
    
  #functions
#4types
#1st type
def add(a,b):
    return a+b
x=add(5,6)
print(x)'''
'''def add(a,b):
    return a+b
print(add(2,4))

#2nd type
def add(a,b):
    print(a+b)

add(7,9)
#3rd type
def add():
    n1=int(input())
    n2=int(input())
    return n1+n2
print(add())
#4th type
def add():
    n1=int(input())
    n2=int(input())
    print(n1+n2)
add()
#add sub mul div
def add(v1,v2):
    return v1+v2

def sub(v1,v2):
    return v1-v2
def mul(v1,v2):
    return v1*v2
def div(v1,v2):
    return v1//v2
while True:
    print("1.add,2.sub,3.mul,4.div")
    ch=int(input("enter choice:"))
    if ch==1:
        a=int(input())
        b=int(input())
        print(add(a,b))
    elif ch==2:
        a=int(input())
        b=int(input())
        print(sub(a,b))
    elif ch==3:
        a=int(input())
        b=int(input())
        print(mul(a,b))
    elif ch==4:
        a=int(input())
        b=int(input())
        print(div(a,b))
    else:
        print("exit program")
        break'''
    
    




