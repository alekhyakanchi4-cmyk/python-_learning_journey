'''n=7
for i in range(1,n+1,2):
    print(" " * (n - i) + "* "*i)'''


#right to left pattern
'''for i in range(1,6):
    for j in range(5-i):
        print(" ",end=" ")
    for k in range(i):
            print("*",end=" ")
    print()'''
    

#top to bottom 5-1 pattern
'''n=5
for i in range(n,0,-1):
    print(" " * (n - i) + "* "*i) ''' 



#or

'''n=4
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()'''


#triangle pattern
'''n=4
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()'''



#diamond
'''n=4
for i in range(1,n+1):
    print(" "*(n-i)+"*"*(2*i-1))
    
for j in range(n,0,-1):
      print(" "*(n-j)+"*"*(2*j-1))'''

#halfbutterfly
'''n=5
for i in range(1,n+1):
    print("*"*i+" "*(2*(n-i))+"*"*i)'''

#butterfly pattern
'''n=5
for i in range(1,n+1):
    print("*"*i+" "*(2*(n-i))+"*"*i)
    
for j in range(n,0,-1):
    print("*"*j+" "*(2*(n-j))+"*"*j)'''
       
         
