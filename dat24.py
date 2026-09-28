
#lambda x:
#1st method to define
print((lambda x:x*x)(5))
print((lambda x:x*x)(10))
#2nd method to define
squ=lambda x:x*x
print(squ(7))
#square
s=[1,2,3,4]
d=list(map(lambda x:x*x,s))
print(d)
#converting to upper
s=["ab","ba"]
d=list(map(lambda x:x.upper(),s))
print(d)
#coverting to smaller
s=["BB","AA"]
d=list(map(lambda x:x.lower(),s))
print(d)

#even
print((lambda x:"even"if x%2==0 else "odd")(4))

#even taking input from user
print((lambda x:"even"if x%2==0 else "odd")(int(input())))
s=[1,2,3,4]
d=list(map(lambda x:"even" if x%2==0 else "odd",s))
print(d)

s=[1,2,3,4,5,6,7,8]
def even(x):
    if x%2==0:
        return x
d=list(filter(even,s))
print(d)
#even
s=[1,2,3,4,5,6,7,8]

d=list(filter(lambda x:  x%2==0,s))
print(d)

#vowels
s=input()
d=list(filter(lambda x: x in "aeiou",s))
print(d)

s=input()
d=list(filter(lambda x:x.lower() in "aeiou",s))
print(list(d))

#reduce method
from functools import reduce
def add(x,y):
    return x+y
s=[1,2,3,4,5]
d=reduce(add,s)
print(d)


#map()  most used
#filter   to filter data
#lambda  perform logic and return single value


from functools import reduce
def add(x,y):
    return x+y
s=[1,2,3,4,5]
d=reduce(lambda x,y:x+y,s)
print(d)
#ascii code
print(ord("h"))
#character upto 122
print(chr(90))

print(chr(420))
#ascii for our name
s="baby"
for i in s:
   print(i,"-->",ord(i))'''
    
'''print(ord("b"))
print(ord("a"))
print(ord("b"))
print(ord("y"))

s="0123456789"
for i in s:
    print(i,"-->",ord(i))
#ascii from 1 to 122
for i in range(1,123):
    print(i,"-->",chr(i))
#capital alpha
for i in range(65,91):
    print(i,"-->",chr(i))



    
