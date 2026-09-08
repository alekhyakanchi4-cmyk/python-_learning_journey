#count of number of words in string
'''s=input()
words=s.split()
print(len(words))'''


#reverse a string

'''s=input()
rev=""
for ch in s:
    rev=ch+rev
print(rev)'''



#check whether a string is palindrome

'''s=input()
rev=""
for ch in s:
    rev=ch+rev
    if s==rev:
        print("palindrome")
    else:
        print("not palindrome")'''


#lists
#1st method
'''lst1=[11,22,"alekhya",65.7,True,False]
print(lst1)
print(type(lst1))
#append
lst1.append(1)
print(lst1)'''

#2nd method
'''s="alekhya"
h=list(s)
print(h)

s="20"
h=list(s)
print(h)'''
#accesing list elements
'''a=[10,20,30]
print(a[1])
print(a[0])
print(a[2])'''



'''b=["l",34,"hhh","ba"]
print(b[2])
print(b[-1])'''
#slicing
'''c=["k",20,56,"b"]
print(c[0:2])'''

#step
'''k=[10,20,30,40,50,60]
print(k[0:7:2])'''


'''s=[10,20,30,40,50,"h"]
print(s[-1:-4:-1])# positive 5:2:-1

print(s[-1:-6:-2])# positive 5:1:-2
print(s[1:7:2])'''#poitive  1:7:2

'''a=[11,22,33,[44,55,66],77]
print(a[3][1])'''


#properties
#concatenation
'''s=[10,20,30]
r=[40,50,60]
h=s+r
print(h)


print([10,20,30]*3)'''


#changing values
'''i=[10,20,30,"a",50,60]
i[2]="alekhya"
print(i)
i[3:6]="kjh"
print(i)'''


'''i=[10,20,30,"a",50,60]
i[3:]=[40]
print(i)'''

'''i=[10,20,30,"a",50,60]
i[0:3]=[90]
print(i)'''

#built in functions
'''s=[10,30,40]
print(len(s))
print(max(s))
print(min(s))
print(sum(s))
print(any(s))
print(all(s))


s=[0,0,0]
print(len(s))
print(max(s))
print(min(s))
print(sum(s))
print(any(s))
print(all(s))

s=[8,9,67,78,67]
print(sorted(s))
print(s.reversed())
#reverse
s=[10,20,30]
s.reverse()
print(s)'''

#methods
#append
'''s=[10,30,20,40,50,10]
print(s.count(10))
s.append(45)
print(s)'''



'''s=[10,30,20,40,50,10]
print(s.count(10))
s.append([45,25])
print(s)'''

#index
'''s=[10,20,30,50,60,10]
print(s.index(10))
print(s.index(10,2))'''

#insert

'''s=[10,20,30,40]
s.insert(2,25)
s.insert(3,"a")
print(s)'''
#remove
'''s=[10,20,30,40,10]
s.remove(10)
s.remove(10)
print(s)'''#[20,30,40]

#pop()

'''s=[10,20,"g",30]
s.pop(2)
print(s)'''#[10,20,30]

#sort()
'''s=[9,23,40,50,8,6]
s.sort()
print(s)'''
#clear()
'''s=[9,23,40,50,8,6]
s.clear()
print(s)'''

#extend
'''s=[90,45,56]
s.extend([10])
print(s)'''
#copy
'''s=[12.23,45]
h=s.copy()
h[0]="h"
print(h)
print(s)'''

#dcopy means orginal also changed
'''s=[90,89,78]
k=s
k[0]="k"
print(k)
print(s)'''

#reverse()

'''s=[10,99,77,88]
s.reverse()
print(s)'''













