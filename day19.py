s=10,5,2,4,3,5,1
print(max(s)-min(s))


s= -1,2,3
print(max(s)-min(s))



s=[10,5,2,4,3,5]
mx=0
for i in s:
    for j in s:
        d=i-j
        if d>mx:
            mx=d
print(mx)

#dictionary
d={}        
d={1:20,2:30,3:40}
print(d)
print(type(d))

d={'1':10,'2':20,'3':30,'4':40}
print(d)
print(type(d))

#duplicate key values
d={'1':10,'2':20,'3':30,'1':40}
print(d)

d={[1,2]:10,[2,2]:20}
print(d)#error because list



d={(10,1):10,(10,2):20}
print(d)


d={{10,1}:10,{10,2}:20}
print(d)#error because set


#accessing values using keys
d={1:10,2:20,3:30,4:40,5:50}
print(d[3])
print(d[1])
print(d[4])
print(d[2])
print(d[5])

#updation
d={1:10,2:20,3:30,4:40,5:50}
d[2]=100
d[5]="alekhya"
print(d)


#adding new key and value pair

d={1:10,2:20,3:30,4:40,5:50}
d["a"]=70
d["b"]="baby"
d["c"]="alekhya"
d[6]=77
print(d)

d={"name":["baby","alekhya"],
   "rol":[10,20],
   }
print(d["name"],d["rol"])
print(d["rol"])

   
