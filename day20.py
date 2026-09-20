s=[1,0,3,0,5,7]
k=[]
for i in s:
    if i>0:
        k.append(i)
    
print(k)
s=[1,0,3,0,5,7]
k=[]
j=[]
for i in s:
    if i==0:
        k.append(i)
    if i>0:
        j.append(i)
res=k+j
print(res)      
#printing zeroes backside        
s=[1,0,3,0,5,7]
k=[]
for i in s:
    if i!=0:
        k.append(i)
for i in s:
    if i==0:
        k.append(i)
print(k)
#del

d={1:20,2:20,3:30,4:40}
del(d[3])
print(d)

d.clear()
print(d)
#accesing only values and keys
d={1:20,2:20,3:30,4:40}
print(d.keys())
print(d.values())

#accesing both values and keys
d={1:20,2:20,3:30,4:40}
s=d.items()
print(s)


d={"name":["baby","alekhya"],
   "rol":[10,20],}
print(d["name"])
print(d["rol"])
#using for loop
d={1:20,2:20,3:30,4:40}
for i in d:
    print(i)
#accesing keys,values and both using keys(),values()
d={1:20,2:20,3:30,4:40}
for k in d.keys():
    print(k)
for v in d.values():
    print(v)
for i in d.items():
    print(i)
#index with keys
d={1:"a",2:20,3:30,4:40}
for i in enumerate(d):
    print(i)

d={"r":20,"i":30,"h":70,"a":80}
print(d.values())
print(sum(d.values()))

#sum
d={1:2,2:20,3:30,4:40}
sum=0
for v in d.values():
    sum=sum+v
print(sum)

#printing vowels in dict
d={"r":20,"i":30,"h":70,"a":80}
for i in d.keys():
    if i in 'aeiou':
        print(i)
    
#input from user  
n=int(input())
d={}
for i in range(n):
    k=input(f"enter key {i+1}:")
    v=input(f"enter val {i+1}:")
    d[k]=v
print(d)
#printing same key to all the values
a=["a","l","e","k","h","Y","a"]
k=2
r=dict.fromkeys(a,k)
print(r)
#get() if key is not present in given dict it return value given in get()
d={"r":20,"i":30,"h":70,"a":80}
print(d.get("k",0))

d={"r":20,"i":30,"h":70,"a":80}
print(d.get("r",0))


d={"r":20,"i":30,"h":70,"a":80}
print(d.get("k",-1)) '''  
#deleting key
'''d={"r":20,"i":30,"h":70,"a":80}
print(d.pop("r"))
print(d)


d={1:20,2:20,3:30,4:40}
del(d[3])
print(d)

d={1:20,2:20,3:30,4:40}
print(d.pop(2))
print(d)
#update

d={"r":20,"i":30,"h":70,"a":80}
d.update({1:20,2:20})
print(d)
d[3]=90
print(d)


#setdefault
d={"r":20,"i":30,"h":70,"a":80}
d.setdefault("t",70)
print(d)
d={"r":20,"i":30,"h":70,"a":80}
d.setdefault("u")
print(d)

#copy
d={"r":20,"i":30,"h":70,"a":80}
s=d.copy()
print(s)
s[9]=90
print(s)
print(d)
