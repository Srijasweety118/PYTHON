#practice questions
#1.Create a class by name circle and find the area and perimeter
# area=pi*r**2
#perimeter=2*pi*r
import math
# r=int(input())
# class Circle:
#     def area(self):
#         area1=(math.pi)*r**2
#         print("area of circle is:",area1)
#     def perimeter(self):
#         perimeter1=2*(math.pi)*r
#         print("perimeter of circle is:",perimeter1) 

# c1=Circle()
# c1.area()
# c1.perimeter()          
        
#2.create a class employee and find the avg salary of employee
# class Employee:
#     def __init__ (self,s1,s2):
#         self.s1=s1
#         self.s2=s2
#         average=(s1+s2)/2
#     def average(self):
#         average=(self.s1+self.s2)/2
#         print("employee average salary",average)
# e1=Employee(10,20)    
# e1.average()        
        
#3.Types of inheritance talking employee class employee
# class Clerk:
#     def name(self):
#         print("Clerk")
#     def id(self):
#         print(123)
# class Manager(Clerk):
#     def qualification(self):
#         print("manager qualification")
# m1=Manager()
# m1.name()
# m1.id()
# m1.qualification()
#multilevel 
# class Clerk:
#     def name(self):
#         print("Clerk")
#     def id(self):
#         print(123)
# class Manager(Clerk):
#     def qualification(self):
#         print("manager qualification")
# class Ceo(Manager):
#     def experience(self):
#         print("Ceo")        
# c1=Ceo()
# c1.name()
# c1.id()
# c1.qualification()
# c1.experience()
#multiple
class Clerk:
    def name(self):
        print("Clerk")
    def id(self):
        print(123)
class Manager:
    def qualification(self):
        print("manager qualification")
class Ceo(Manager,Clerk):
    def experience(self):
        print("Ceo")        
c1=Ceo()
c1.name()
c1.id()
c1.qualification()
c1.experience()
#4.method overriding
# class Student():
#     def Akhil(self):
#         print("akhil")
            
# class Friend(Student):        
#     def Akhil(self):
#         print("khaja")

# f1=Friend()
# f1.Akhil()         
#with using super keyword
class Student():
    def Akhil(self):
        print("akhil")
            
class Friend(Student):        
    def __init__(self):
        super().Akhil()
    def Akhil(self):
        print("khaja")

f1=Friend()
f1.Akhil()         

#5.create a inner class Levelup and two inner classes python,html and access the course name
class Levelup:
    def __init__(self,course):
        self.course=course
    def core(self):
        print(self.course)    
    class Python:
        def __init__(self,name):
            self.name=name 
        def display(self):
            print("BACKEND COURSE IS:",self.name)
    class Html:
        def __init__(self,name1):
            self.name1=name1
        def display(self):
            print("Fronted course is :",self.name1)
l=Levelup("FSD")
c=l.Python()
c.display()
a=l.Html()
a.display()
