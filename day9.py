#armstrong number
'''num=int(input())
temp=num
num_digits=len(str(num))
digit_sum=0
while temp>0:
    digit=temp%10
    digit_sum+=digit**num_digits
    temp//=10
if num==digit_sum:
        print("it is arm strong number")
else:
        print("not armstrong number")'''


'''#lcm of 2 numbers

num1=int(input())
num2=int(input())
a,b=num1,num2
while b!=0:
    a,b=b,a%b
gcd=a
lcm=(num1*num2)//gcd
print("gcd:",gcd)
print("lcm:",lcm)'''


#prime numbers between range
'''x=int(input())
y=int(input())
for num in range(x,y+1):
    if num>1:
        is_prime=True
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                is_prime=False
                break
            if is_prime:
                print(num,end=" ")
print()'''
#strong number or not
'''num=int(input())
temp=num
strong_sum=0
while temp>0:
    digit=temp%10
    fact=1
    for i in range(1,digit+1):
        fact*=i
    strong_sum=strong_sum+fact
    temp//=10
if strong_sum==num:
    print("num is strong number")
else:
    print("num is not strong number")'''
#find the nth prime number
'''n=int(input())
count=0
candidate=1
while count<n:
    candidate+=1
    is_prime=True
    
    for i in range(2,int(candidate**0.5)+1):
        if candidate%i==0:
            is_prime=False
            break
    if is_prime:
            count+=1
print(f"the {n}th prime number is {candidate}")'''


    
