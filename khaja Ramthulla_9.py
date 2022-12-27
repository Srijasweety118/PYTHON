# '1.Write a Python program to find the Area of Triangle.
#    semi-perimeter : s=(a+b+c)/2
#   (formula to find area of traingle  is area = (s*(s-a)*(s-b)*(s-c))**0.5)'''

a=10
b=20
c=30
a=float(input("enter the area of triangle"))
b=float(input("enter the area of triangle"))
c=float(input("enter the area of triangle"))
s=a+b+c/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print(' the area of triangle',area)

# ​
# '''2.Write a Pyhton program to capture employee details like emp_id,emp_name and emp_salary
#   and display them.'''
a=input("enter the empname")
b=int(input("enter the empsalary"))
c=int(input("enter the empid"))
print("empname",a)
print("empsalary",b)
print("empid",c)
# #3.Write a program to calculate the average of three numbers taking user input.
a=int(input("enter the average"))
b=int(input("enter the average"))
c=int(input("enter the average"))
a=(a+b+c)/3
print("average of a number ",a)
print("average of b number ",b)
print("average of c number ",c)
# '''4.Write a program to calculate the compound Interest.
# #    CI=P(1+R/100)^t'''
P=float(input("enter the priciple amount"))
R=float(input("enter the rate of intreset"))
t=float(input("enter the time "))
a= (P*(1+(R/100)))**t
print(a)
CI=a-P
print(CI)
   
# #5.Write a program to represent integer 20 into binary,hexadecimal and octal.
a=20
print(bin(a))
print(hex(a))
print(oct(a))
# #6.Write a program to calculate square root of a number. (square root = number ** 0.5)
number=int(input("enter the number"))
sr=number**0.5
print(" square number",sr)
# '''7.Write a program to calculate Simple Interest by taking user input
#     si=(p*t*r)/100'''

p=float(input("enter the p"))
t=float(input("enter the time"))
r=float(input("enter the rate"))
si=(p*t*r)/100
print("enter the p",si)
# #8.Write a program to calculate the Area of circle using math module
pi=3.142
r=float(input("enter the value of radius"))
a=pi*r*r
print("enter are of circle=",a)

# #9.Demonstrate the following with example
#    1.reading an expression
from this import d


a=int(input("enter the number"))
print(a)
#    2.reading char
c=input("enter name")
print(c)
# 3.reaading multiple inputs
a=int(input("enter the number"))
print(a)
b=int(input("enter the number"))
print(b)
c=int(input("enter the number"))
print(c)
d=int(input("enter the number"))
print(d)
#    4.use of format method
age=21
txt="my name is john and my age is{}"
print(txt.format(age))

