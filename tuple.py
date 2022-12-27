#tuple is sequence/collection which is ordered and indexed
#tuples are immutable it can't ba changed
#the tuple can be indicated as '()
 
#create a tuple
from audioop import reverse

tpl=(10,)
print(tpl)
print(type(tpl))
#indexing()
tpl=(10,20,30,40,50)
print(tpl[1])
print(tpl[0])
#slicing()
tpl=(10,20,30,40,50)
print(tpl[0:])
print(tpl[:3])
#repeatation
print(tpl*3)
#length of the tuple
print(len(tpl))
# If we can't perform methods such as insert(),append(),remove(),pop(),clear()..
#change the values
x=('python','django','java')
print(x)
y=(list(x))
print(y)
y[2]='javascript'
print(y)
z=tuple(y)
print(z)
#nested tuple
tple=('hello','hii',(1,2,3),('xyz'))
print(tple[0])
print(tple[3])
print(tple[0])
print(tple[1])
#memership operators
tpl=(10,20,30,40,50)
print(1 in tpl)
print(10 in tpl)
print(100 not in tpl)
#tuple constructor
mytpl=tuple(('rose','jasmine','lotus'))
print(mytpl)
#tuple methods index(),
t1=(1,2,3,4,4,5,67,8)
print(t1.index(4)) # it will gives a error, because index() values are not supported in tuples
#tuple concatination
t1=(1,2,3)
t2=(4,5,6)
t3=t1+t2
print(t3)
print((1,2,3)+t2)
#adding elements into tuple
t=('audi','bmw')
t1=list(t)
t1.append('benz')
print(t1)