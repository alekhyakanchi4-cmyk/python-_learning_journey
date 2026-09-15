#15/9

#tuple
#we cannot change the data
#immutaable datatype
#()
#1st way
s=(1,2,3)
print(s)
print(type(s))

#2nd way
#we should seperte with , if one element exist
s=(10,)
print(s)

#3rd way
s=10,20,30
print(s)

#4th way
s="sree vahini"
a=tuple(s)
print(a)

a="alekhya"
b=tuple(a)
print(b)

s="aaa"
print(tuple(s))



#accesing elements
s=(10,20,30,"a","b",40)
print(s[4])
print(s[-1])
print(s[3:])

print(s[::-1])
print(s[::-2])

#extracting middle element in any length
s=(10,20,30,"a","b",40)
l=len(s)
middle=l//2
print(s[middle])

#concatination
s=(10,20,30,"a","b",40)
a=(30,40)
print(s+a)


#repeatition *
s=(10,20,30,"a","b",40)
print(s*2)
#changing values in the tuple that are in list
s=(10,20,"h",[40,50,60],30)
print(s)
print(s[3])
print(s[3][0])

print(s[3][1])
print(s[3][2])
s[3][0]=90
print(s)

#tuple is speed compared to list becUSE OF memory allocation list alloctes more memory
#nested tuples
#looping in tuples
s=(10,20,30,40,50)
for i in s:
    print(i)


s=(10,20,30,40,50)
for i in s:
    print(i,end=" ")

#while
s=(10,20,30,40,50)
i=0
n=len(s)
while i<n:
    print(s[i])
    i=i+1  


s=(10,20,30,40,50)
i=0
n=len(s)
while i<n:
    print(s[i],end=" ")
    i=i+1



#using range

s=(1,2,3,4,5)
for i in range(len(s)):
    print(s[i])

#enumareate
s=(1,2,3,4,5)
for i,j in enumerate(s):
    print(i,j)

#lhs=rhs
name,details,branch="baby",23,"ds"
print(name,details,branch)

#tuple packing

name,*details="baby",23,"ds"
print(name,details)
*name,details="baby",23,"ds"
print(name,details)

n=int(input())
res=()
for i in range(n):
    v=int(input())
    res=res+tuple(v)
print(res)
#taking input from user
n=int(input())
t=()
for i in range(n):
    value=input()
    if value.isdigit():
        value=int(value)
    t=t+(value,)
print(t)
#2nd method
n=int(input())
res=[]
for i in range(n):
    v=int(input())
    res.append(v)
print(tuple(res))
#3rd method
n=int(input())
tpl=()
for i in range(n):
    v=int(input())
    tpl=tpl+(v,)
print(tpl)

#even
s=(1,2,3,4,5,6)
for i in s:
    if i%2==0:
        print(i)

#even
n=int(input())
t=()
for i in range(n):
    value=int(input())
    if value%2==0:
        t=t+(value,)
print(t)
#tuple comprehension
s=(1,2,3,4,5,6)
print(tuple(i for i in s if i%2==0))
#suares
s=(1,2,3,4,5)
sq=[]
for i in s:
    squ=i**2
    sq.append(squ)
print(tuple(sq))
#list comprehension 
s=(1,2,3,4,5)
print(tuple(i**2 for i in s))


