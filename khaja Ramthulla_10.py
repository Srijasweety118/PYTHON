# 1.Write python program to find the largest of three numbers.
num1=float(input("enter first number"))
num2=float(input("enter the second number"))
num3=float(input("enter the third number"))
if(num1>num2) and(num1>num3):
    largest_num=num1
elif(num2>num1)and(num2>num3):
    largest_num=num2
else:
    largest_num=num3
    print("enter the largest number",largest_num)
# 2.Write a python program to check whether a person can get a driving license (consider age to be 18 and above)
b=int(input("enter the age"))
if(b>=18):
    print("you are eligible for driving license")
else:
    print("you are not eligible for driving license")
#3.Write a program to check student result for below marks and display grade
'''90 or above is equivalent to an A grade
  80-89 is equivalent to a B grade
  70-79 is equivalent to a C grade
  65-69 is equivalent to a D grade
  64 or below is equivalent to an F grade'''
marks=int(input("enter your marks"))
if (marks>=90):
    print("A grade",marks)
elif marks>=80 and marks<89:
    print("B grade",marks)
elif marks>=70 and marks<79:
    print("C grade",marks) 
elif marks>=65 and marks<69:
    print("D grade",marks)
else:
    print("F grade")