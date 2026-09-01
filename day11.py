#palindrome
'''n=int(input())
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(1,i+1):
        print(j,end="")
    for j in range(i-1,0,-1):
        print(j,end="")
    print()'''



#square pattern
'''n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print("*",end=" ")
            
        else:
            print(" ",end=" ")
    print()'''



#traingle
'''n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==n or j==1 or j==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''


#traingle
'''n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==n or j==n or i+j==n+1:
            
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''



#cross
'''n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or i+j==n+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

#plus symbol
'''n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==3 or i==3:
             print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''




#break


'''for i in range(1,11):
    print(i)
    if i==11:
        break
else:
    print("loop completed")'''
            



'''for i in range(1,11):
    print(i)
    if i==10:
        break
else:
    print("loop completed")'''

            
 #continue   
'''for i in range(1,11):
    print(i)
    if i==5:
        continue
else:
    print("loop completed")'''



'''for i in range(1,11):
    if i==5:
        continue
    print(i)'''
                        
'''for i in range(1,11):
    if i==5:
        continue
    print(i)
else:
    print("loop completed")'''

#the else with loops
'''for num in range(5):
    print(f"current number:{num}")
else:
    print("loop completed successfully")'''



'''for num in range(5):
    print(f"current number:{num}")
    if num==3:
        break
else:
    print("loop completed normally")'''



#else using while loop
'''count=0
while count<10:
    print(f"current count{count}")
    count=count+1
else:
    print("loop completed normally")'''

count=0
while count<10:
    print(f"current count{count}")
    count=count+1
    if count>5:
        break
else:





