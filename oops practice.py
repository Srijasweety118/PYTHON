#1.multiple inheritance
class Clerk:
    def name(self):
        print("Clerk")
class Manager(Clerk):
    def qualification(self):
        print("Manager")
class Ceo(Manager):
    def experience(self):
        print("Eco qualification") 
c1=Ceo()
c1.name()
c1.qualification()
c1.experience()        

#2.inheritance attribute/properties and functionalities/methods
class Car:
    def __init__(self,make,model):
        self.make=make
        self.model=model
    def color(self):
        print("blue")
class Engine(Car):
    def __init__(self,year,make,model):
        Car.__init__(self,make,model)
        self.year=year
e1=Engine(2020,'bmw','208i')
e1.color()
print(e1.make)
print(e1.model)
print(e1.year)
#encapsulation
class Student():
    def __init__(self):
        self._name="khaja"
        self._id=123
    def display(self):
        print(self._name)
        print(self._id)
s1=Student()
s1.display()

#polymorphism

class Duck:
    def talk(self):
        print("quack")
class Human:
    def talk(self):
        print("hello")
def callTalk(obj):
    obj.talk()
d=Duck()
callTalk(d)
h=Human()
callTalk(h)    

#average of

class Bike:
    def __init__(self,price1,price2):
        self.price1=price1
        self.price2=price2
    def average(self):
        print((self.price1+self.price2)/2)        
b=Bike(50000,10000)
b.average()

#6.palindrom string MAdam
str = 'MADAM'
rev = reversed(str)
if list(str) == list(rev):
 print("PALINDROME !")

else:
 print("NOT PALINDROME !")

#7.
lst=[1,2,3,4,5,13,15,39,23,25]
for i in lst:
    if(i%5)==0:
        print(i)
for j in lst:
    if(j%3)==0:
        print(j)  

#8. chack if a file exist
