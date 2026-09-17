#program for printing index numbers whose sum is equal to target
a=[5,10,7,1,6,3]
target=8
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==target:
            
            print(i,j)
        break

#set
s={10,20,20,30}
print(s)

s={10,20,"h",True,10}
print(s)
h=set("sreevahini")
print(h)

d=set()
print(d)
#using loops
s={10,"h","r","d",30,50}
for i in s:
    print(i)


s={10,"h","r","d",30,50}
for i in s:
    print(i,end=" ")

#using enumerate
s={10,"h","r","d",30,50}
for i,j in enumerate(s):
    print(i,j)



#length of a set
a={1,2,3,4}
print(len(a))

#length
a={1,2,3,4,5}
count=0
for i in range(len(a)):
    count=count+1
print(count)

#sum
a={1,2,3,4}
sum=0
for i in a:
    sum=sum+i
print(sum)
#string values as input
d={"a","b"}
s=""
for i in d:
    s=s+i
print(s)


#adding elements to the set   add()
s={10,20,30}
s.add(40)
s.add("alekhy'''

#copy
s={10,20,30}
h=s.copy()
h.add(40)
print(s)
print(h)

#clear to arase all the data
s={10,20,30}
s.clear()
print(s)

#remove
s={10,20,30,40}
s.remove(20)
print(s)


#discard
s={10,20,30,40}
s.discard(30)
print(s)
#pop
s={10,20,30,50,60}
print(s.pop())
print(s)

#update
s={10,20,30,40}
s.update([40,0,50])
print(s)


#adding values to set through user
n=int(input())
res=[]
for i in range(n):
    v=int(input())
    res.append(v)
print(set(res))


#methods
#union(|)

s1={10,20,30}
s2={40,50,60}
print(s1.union(s2))

#intersection
s1={10,20,30}
s2={40,50,30}
print(s1.intersection(s2))
#difference
s1={10,20,30}
s2={10,50,60}
print(s1.difference(s2))

#intersection update
#difference_update
#symmetricdifference_update


#issubset
#is superset
#is disjoint

s1={10,20,30}
s2={10,40,30,60,20}
s1.intersection_update(s2)
print(s1)

#set 2 lo diff ga unayii

s1={10,20,30,90}
s2={10,40,30,60,20}
s1.difference_update(s2)
print(s1)
#set 1 2 compare chesi different ga unayii while                                                            

s1={10,20,30,80}
s2={10,40,30,60,20}
s1.symmetric_difference_update(s2)
print(s1)








