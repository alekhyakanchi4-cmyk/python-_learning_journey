'''
procedural languages
functional
object oriented
'''
'''
classes and objects
structed data is taken from user stored in class
provides privacy
clss is blueprint
object is instance of clss
'''
'''class student():
    a=10'''

    
'''class student():
    clg="vahini"
    def course():
        print("ds")
course()'''


#defining class
class laptop:
    clr="black"
    length=9
    shape="square"
    def work():
        print("do coding")
m=laptop()
print(m.clr)
print(m.length)
print(m.shape)
m2=laptop()
print(m2.clr)




class laptop:
    clr="black"
    length=9
    shape="square"
    def work(self):
        print("do coding")
m=laptop()
print(m.clr)
print(m.length)
print(m.shape)
m.work()
m2=laptop()
m2.work()



#sum usiing class
#taking diff inputs
class laptop:
    cmp="hp"
    def Laptop(self,clr,length,shape):
        self.clr=clr
        self.length=length
        self.shape=shape
    def show(self):
        print(self.clr,self.length,self.shape)
m=laptop()
m.Laptop("white",10,"squ")
m.show()
#2nd obj
m2=laptop()
m2.Laptop("black",20,"squ")
m2.show()
#init =consructor
class laptop:
    cmp="hp"
    def __init__(self,clr,length,shape):
        self.clr=clr
        self.length=length
        self.shape=shape
    def show(self):
        print(self.clr,self.length,self.shape)
m=laptop("white",10,"squ")
m.show()
#2nd obj
m2=laptop("black",20,"squ")
m2.show()

#bank details
class bankname:
    bname="SBI"
    def Bank(self,bankname,name,acc_no,ifsc,balance):
        self.bankname=bankname
        self.name=name
        self.acc_no=acc_no
        self.ifsc=ifsc
        self.balance=balance
    def show(self):
        print(self.bankname,self.name,self.acc_no,self.ifsc,self.balance)
m=bankname()
m.Bank("sbi","alekhya",4410,345,12000)
m.show()


#bank details
class bankname:
    bname="SBI"
    def __init__(self,bankname,name,acc_no,ifsc,balance):
        self.bankname=bankname
        self.name=name
        self.acc_no=acc_no
        self.ifsc=ifsc
        self.balance=balance
    def show(self):
        print("bankname  :",self.bankname)
        print("name      :" ,self.name)
        print("acc_no    :",self.acc_no)
        print("ifsccode  :",self.ifsc)
        print("amount    :",self.balance)
m=bankname("sbi","alekhya",4410,345,12000)
m.show()
m2=bankname("sbi","balakrishna",4411,354,13000)
m2.show()

m3=bankname("canara","harish",4423,"trtr56",14000)
m3.show()


#deposit

class bankname:
    bname="SBI"
    def __init__(self,bankname,name,acc_no,ifsc,balance):
        self.bankname=bankname
        self.name=name
        self.acc_no=acc_no
        self.ifsc=ifsc
        self.balance=balance
    def deposit(self,amount):
        self.amount=amount
        self.balance=self.balance+self.amount
        print(self.balance)
    def show(self):
        print("bankname  :",self.bankname)
        print("name      :" ,self.name)
        print("acc_no    :",self.acc_no)
        print("ifsccode  :",self.ifsc)
        print("amount    :",self.balance)
m=bankname("sbi","alekhya",4410,345,12000)
m.deposit(1000)
#deposit and withdraw
class bankname:
    bname="SBI"
    def __init__(self,bankname,name,acc_no,ifsc,balance):
        self.bankname=bankname
        self.name=name
        self.acc_no=acc_no
        self.ifsc=ifsc
        self.balance=balance
    def deposit(self,amount):
        self.amount=amount
        self.balance=self.balance+self.amount
        print(self.balance)
    def withdraw(self,amount):
        self.amount=amount
        self.balance=self.balance-self.amount
        print(self.balance)
    
    def show(self):
        print("bankname  :",self.bankname)
        print("name      :" ,self.name)
        print("acc_no    :",self.acc_no)
        print("ifsccode  :",self.ifsc)
        print("amount    :",self.balance)
m=bankname("sbi","alekhya",4410,345,12000)
m.deposit(1000)
m.withdraw(1000)


#withdraw
class bankname:
    bname="SBI"
    def __init__(self,bankname,name,acc_no,ifsc,balance):
        self.bankname=bankname
        self.name=name
        self.acc_no=acc_no
        self.ifsc=ifsc
        self.balance=balance
    def withdraw(self,amount):
        self.amount=amount
        self.balance=self.balance-self.amount
        print(self.balance)
    def show(self):
        print("bankname  :",self.bankname)
        print("name      :" ,self.name)
        print("acc_no    :",self.acc_no)
        print("ifsccode  :",self.ifsc)
        print("amount    :",self.balance)
m=bankname("sbi","alekhya",4410,345,12000)
m.withdraw(1000)
#insuficent balance
class bankname:
    bname="SBI"
    def __init__(self,bankname,name,acc_no,ifsc,balance):
        self.bankname=bankname
        self.name=name
        self.acc_no=acc_no
        self.ifsc=ifsc
        self.balance=balance
    def deposit(self,amount):
        self.amount=amount
        self.balance=self.balance+self.amount
        print(self.balance)
    def withdraw(self,amount):
        self.amount=amount
        if self.amount<self.balance:
            self.balance=self.balance-self.amount
            print("transcaton successfull")
        else:
            print("insuffiencet balance")
        print("totalbalance:",self.balance)
    
    def show(self):
        print("bankname  :",self.bankname)
        print("name      :" ,self.name)
        print("acc_no    :",self.acc_no)
        print("ifsccode  :",self.ifsc)
        print("amount    :",self.balance)
m=bankname("sbi","alekhya",4410,345,12000)
m.deposit(1000)
m.withdraw(100000)



#oops
'''
inheritance=5types
encapsulation
abstraction
polymorphism'''

#single inheritance
class Person:
    def walk(self):
        print("walking")
    def eating(self):
        print("eating cookies")
    def sleep(self):
        print("sleeping")
class student(Person):
    def read(self):
        print("reading")
p=student()
p.walk()
#multilevel
class Person:
    def walk(self):
        print("walking")
    def eating(self):
        print("eating cookies")
    def sleep(self):
        print("sleeping")
class student(Person):
    def read(self):
        print("reading")
class professional(Person):
    def work(self):
        print("working")
    def login(self):
        print("incoming")
    def salary(self):
        print("salary")

p=professional()
p.walk()
p.eating()
p.salary()
q=student()
q.walk()
r=Person()
r.salary()








