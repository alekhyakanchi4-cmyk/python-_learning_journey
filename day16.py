#while loop
s=[10,20,30,40,50]
i=0
n=len(s)
while i<n:
    print(s[i])
    i=i+1    
#for    
s=[10,20,30,40,50]
for i in s:
    print(i)
#max
s=[10,2,3,22,5]
print(max(s))
#maximum
s=[10,2,3,22,5]
max=0  
for i in s:
    if i>max:
        max=i
print(max)
#min
s=[10,2,3,22,5]
min=s[0]
for i in s:
    if i<min:
        min=i
print(min)
#sum
s=[10,2,3,22,5]
sum=0
for i in s:
    sum=i+sum
print(sum)
#even count
s=[10,2,3,22,5]
even=0
for i in s:
    if i%2==0:
        even=even+1
print(even)

#odd count
s=[10,2,3,22,5]
even=0
for i in s:
    if i%2!=0:
        even=even+1
print(even)
#min
s=[10,-2,-1,0,20,5]
min=s[0]
for i in s:
    if i<min:
        min=i
print(min)

#finding index and values

lst=[10,20,30,40,50]
for i in range(len(lst)):
    print(i,lst[i])


#enumerate take two values
s=[10,2,3,22,5]
for i,j in enumerate(s):
    print(i,j)

#using range
lst=[10,20,30,40,50]
for i in range(len(lst)):
    print(lst[i],end=" ")

#with out range
lst=[10,20,30,40,50]
for i in lst:
    print(i,end=" ")

#side by side index and value  
lst=[10,20,30,40,50]
for i in range(len(lst)):
    print(i,lst[i],end=" ")

#even numbers in list
s=[1,2,3,4,5,6,7,8,9,10]
even=[]
for i in s:
    if i%2==0:
        even.append(i)
print(even)
#odd numbers in list
s=[1,2,3,4,5,6,7,8,9,10]
odd=[]
for i in s:
    if i%2!=0:
        odd.append(i)
print(odd)

#using odd+[i]
s=[1,2,3,4,5,6,7,8,9,10]
odd=[]
for i in s:
    if i%2!=0:
        odd=odd+[i]
print(odd)
#list comprehension
#even
s=[1,2,3,4,5,6,7,8]
l=[i for i in s if i%2==0]
print(l)

#odd
s=[1,2,3,4,5,6,7,8]
l=[i for i in s if i%2!=0]
print(l)

#squares
s=[1,2,3,4,5]
sq=[]
for i in s:
    squ=i*i # or  i**2
    sq.append(squ)
print(sq)
#square using list comprehension
s=[1,2,3,4,5]
r=[i**2 for i in s]
print(r)


#input from user
n=int(input())
res=[]
for i in range(n):
    v=int(input(f"enter value {i+1}:"))
    res.append(v)
print(res)


#positive and negative

s=[10,-20,30,-40,60,70,-3]
pos=[]
neg=[]
for i in s:
    if i>0:
        pos.append(i)
    else:
        neg.append(i)
print(pos)
print(neg)
#duplicate
s=[10,20,30,40,50,10,50]
for i in set(s):
    if  s.count(i)>=1:
        print(i)



#ip=[10,20,30,40,50]
#op=[30,40,50,10,20]
#op=[40,50,10,20,30]

s=int(input())
rot=int(input())
for i in s:
    



