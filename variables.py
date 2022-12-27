#variables are box/container for storing values
a=10
b=a
print(a)
print(b)
#case sensitivity
name="khaja"
Name="khaja"
NAME="khaja"
print(name,Name,NAME)
#we cannot have const variables in python
pi=3.142
print(pi)


pi=2.435
print(pi)

#more on variable

a=10
b=a
print(a)
print(b)

print(id(a))#id() returns memory address of variable
print(id(b))

c=20
print(c)
print(id(c))


#1. multiple variables ,single assignment
a=b=c=5
print(a,b,c)
#2. multiple variables ,multiple assignment
a=5
b=5
c=7
print(a,b,c)
a,b,c,d=1,2,3,4
print(a,b,c,d)
#types and value
a=100
print(type(a))
#python supports wide range of data types
#1. None type
a=None
print(a)
print(type(a))
#numeric types 

#compex data type
c=1+2j # 1 is real part ,2j is imaginary part and j is standard co-efficent
print(c)
print(type(c))
#booleans
d=True
print(d)
print(type(d))
#Reprasent number in different formats - binary ,hexa ,octal
print(bin(10))
print(hex(10))# it wii represents 1 to 9 it will displays same after that we can write 10 i will becomes a
print(oct(10))
#type conversation-converting one data type into another datatype
#convert a floating point nmber 
a=10.5
print(a)
print(type(a))
b=int(a)
print(b)
print(type(b))
#convert string to integer
x='10'
print(x)
print(type(x))

y=int(x)
print(y)
print(type(y))