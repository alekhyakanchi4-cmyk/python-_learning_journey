#if statement:
#1
a=int(input())
if a>1000:
    print(a-500)

#2
amount=int(input())
if amount>1000:
    amount=amount-500
print(amount)

#3
per_of_stu=int(input())
if per_of_stu<75:
    print("students  below 75")


#even odd
#1
a=int(input())
if a%2==0:
    print("even")
else:
    print("odd")

#2
a=int(input())
if a%2!=0:
    print("odd")
else:
    print("even")
#3
a=int(input())
if a%2==1:
    print("odd")
else:
    print("even")



#4
a=int(input())
if a%2!=1:
    print("even")
else:
    print("odd")
#5
a=int(input())
if a%2:
    print("odd")
    
#password&username
username=input()
password=int(input())
name="alekhya"
pasw=1234
if username==name and password==pasw:
    print("grant access")
else:
    print("deny access")
#vote
age=int(input())
if age>=18:
    print("eligible for vote:")
else:
    print("not eligible:")
#positive
number=int(input())
if number>=0:
    print("positive")
else:
    print("negative")

#divisible by 5
number=int(input())
num=number%10
if num==0 or num==5:
    print("divisible by 5")
else:
    print("not divisible by 5")


#salary
salary=int(input())
bonus=10
bonus_per=salary*bonus/100
if salary>50000:
    print(salary+bonus_per)
    
#printing how many notes contains for a certain amount
amount=int(input())
nfivehun=amount//500
amount=amount%500
ntwohun=amount//200
amount=amount%200
nhun=amount//100
amount=amount%100
nfif=amount//50
amount=amount%50
ntwen=amount//20
amount=amount%20
nten=amount//10
amount=amount%10
print("500 notes:",nfivehun)
print("200 notes:",ntwohun)
print("100 notes:",nhun)
print("50 notes:",nfif)
print("10 notes:",nten)
print("remaining amount:",amount)
totalnotes=nfivehun+ntwohun+nhun+nfif+nten
print("total notes:",totalnotes)

#discount applicable or not
day=input()
if day=="saturday" and "sunday":
    print("discount applicable:")
else:
    print("no discount:")



    
#vowel or not    
char=input()
if char =='a' or char=='e' or char=='i' or char=='o' or char=='u':
    print("character is vowel:")
else:
    print("character is consonant")
    
#electricity bill
elebill=float(input())
ebill=elebill-(elebill%100)*5+(elebill%100*8)
if elebill<=100:
    print("bill:",elebill*5)
else:
    print("bill:",elebill*8)


#match case
    
n=int(input())
match n:
    case 8:
        print("eight")
    case 6:
        print("six")
    case _:
        print("default case")

#2
n=int(input())
match n:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thursday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case 7:
        print("sunday")
    case _:
        print("not valid")



#nested if
marks=int(input())
if marks>=35:
    if marks>=75:
        print("dist")
    else:
        print("pass")
else:
    print("fail")


num=int(input())
if num>=0:
    if num>0:
        print("positive")
    else:
        print("zero")
else:
    print("negative")









else:
    print("even")
