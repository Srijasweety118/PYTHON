#1. write a python program to append a list to a second list
lst=[1,2,3,4,5]
lst2=[12345]
lst.append(lst2)
print(lst)

#2.write a python program to sum all items in dictionary
dict={'one':1,'Two':2,'Three':3,'Four':4}
for i in dict.items():
    a = sum(dict.values())
print(a)
#3.write a python function to return all arthematic operations
def function():
  a=int(input("enter a value:"))
  b=int(input("enter b value:"))  
  print("add value of",a+b)  
  a=int(input("enter a value:"))
  b=int(input("enter b value:"))  
  print("sub value of",a-b)  
a=int(input("enter a value:"))
b=int(input("enter b value:"))  
print("mul value of",a*b)  
a=int(input("enter a value:"))
b=int(input("enter b value:"))  
print("division value of",a/b)  
a=int(input("enter a value:"))
b=int(input("enter b value:"))  
print("floor value of",a//b)  
a=int(input("enter a value:"))
b=int(input("enter b value:"))  
print("remainder value of",a%b)  
a=int(input("enter a value:"))
b=int(input("enter b value:"))  
print("power value of",a**b)  
  
function()

#4.write a python program to find largest number among three numbers

a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))
if (a>b and a>c):
  print("a is largest number")
elif(b>a and b>c):
     print("b is largest number")
else:
    print("c is largest number")   

#5.write a python program to calculate length of the string with and without()      
s='python is easy'
print(len(s))
#without len()
a= "python is easy"
count=0
for i in a:
     count+=1
     print(count)


#6. write a python program to generate multiplication table if a given number
a=int(input("enter the number"))
for i in range(1,11):
    print(a, "*",i, "=", a*i) 
#7. write a python program to print even numbers i a list using while loop,for loop and lambda function   
list=[1,2,3,4,5,6]
a=0
while a< len(list):
 if a%2==0:
    print(a)
    a=a+1
#for loop
lst=[1,2,3,4,5,6,7,8,9,0]
for i in lst:
 if i%2==0:
         print(i)
lst = [1,2,3,4,5,6,7,8,9,10]
a= list(filter(lambda x: x%2==0,lst))
print(a)   
#8.write a python program to check if a is prime or not 
a=int(input("enter the a value:")) 
for i in range (2,a):
    if(a%i==0):
        print("not prime")
        break;
else:
    print("prime") 
#9. split the string  wherever you find instance of separator 
s="life is precious"
print(s.split(","))        
#10. arrange the list in ascending order
lst=[1,2,'cool',-1,0,-3,10]
lst.sort(reverse=True)
print(lst)         
