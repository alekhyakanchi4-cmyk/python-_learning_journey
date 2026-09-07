#string methods
'''s="Alekhya"
print(s.isalpha())
s="1233"
print(s.isdigit())
s="Alekhya"
print(s.isupper())
print(s.islower())
s="566jkl"
print(s.isalnum())
s="kanchi alekhya"
print(s.startswith("k"))
print(s.endswith("ya"))

a="alekhya"
print(a.islower())'''
#counting alpha,digits,specialcharacter 
'''n=input()
alpha_count=0
digit_count=0
special_count=0
special_characters="@#$%^&*"
for i in n:
    if i.isalpha():
        alpha_count=alpha_count+1
    elif i.isdigit():
        digit_count=digit_count+1
    else:
        special_count=special_count+1
print(alpha_count)
print(digit_count)
print(special_count)'''



#alpha lower upper count
'''n=input()
alpha_count=0
upper_count=0
lower_count=0
special_count=0
for i in n:
    if i.isalpha():
        alpha_count=alpha_count+1
    if i.isupper():
        upper_count=upper_count+1
    if i.islower():
        lower_count=lower_count+1    
    else:
        special_count=special_count+1
print(alpha_count)
print(upper_count)
print(lower_count)'''


#find
''''s="python is a popular language"
print(s.find("is"))
print(s.find("is",11,20))
#replace
print(s.replace("popular","easy"))'''







    
