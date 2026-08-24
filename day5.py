n=int(input())
total=0
for i in range(n):
    num=int(input(f"enter value of {i+1}:"))
    total=total+num
avg=total/n
print(avg)
#pass or fail and distnction or not
marks = int(input())
if marks >= 85:
    if marks >= 90:
        print("distinction")
    else:
        print("pass")
else:
    print("fail")
#even or not
num = int(input())

if num > 100:
    if num % 2 == 0:
        print("even")
    else:
        print("odd")
else:
    print("number less than 100")
#largest number using nested if
a = int(input())
b = int(input())
c = int(input())
if a > b:
    if a > c:
        print("a is larger")
    else:
        print("c is larger")
else:
    if b > c:
        print("b is larger")
    else:
        print("c is larger")
#traingel or not
a = int(input())
b = int(input())
c = int(input())
if a == b:
    if a == c:
        print("triangle")
    else:
        print("not triangle")
else:
    print("invalid")
