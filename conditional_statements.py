# flow control statements will determine the order in which statements are excuted in runtime.
#conditional statements- evaluates wuntil condition is evaluated to true
# control flow structure will make us to colon and identification
# in conditional statemets we have 3 types they are 1.if,2.if else,3.if elif else
#syntax of if statement

if 1<2:
    print('yes')
    if 2<3:
        print("hi")
        if 3<4:
            print("hello")
# syntax of if else
#if condition
#code
#else:
#else block code
if 2>4:
    print("if block")
else:
    print("else block")

    # syntax of if elif else
if 2<4:
     print("true")
elif 3!=3:
     print("f")
else:
    print("else block")    
        # elif ladder
name='john'
if name=='bob':
     print('hi bob')
elif name=='boll':
     print("hi boll")
elif name=='john':
     print('hi john')    
elif name=='hi':
     print("hello")
else:
  print("arey entra bhai edi")   

x=int(input("enter ur number"))
if x==0:
    print(x, "is zero") 
#assignment
a=int(input("enter the number"))
if(a%2)==0:
    print("it is even")
else:
    print("it is odd")