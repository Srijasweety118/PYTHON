#sets are collections which are unordered and unindexed
#it is used to dispaly the sets '{}'
#sets doesn't support multiple items/duplicate items

#create a set
s={10,20,30,'xyz',10,20}
print(s) 
print(type(s))

#sets doesn't support indexing
#sets doesn't support slicing,repetition

#add items to the set
s.add(30)
print(s)
# update()
s.update([50,60,34,44,56])
print(s)
#remove items from the set
s.remove(30)
print(s)

s.discard(50)
print(s) # it is removing the elements in the set
#pop()
s1={'abc','xyz','pqr'}
print(s1)
x=s1.pop()
print(x)
print(s1)
#copy() set into another set 
s1={1,2,3}
print(s)
s2=s1.copy()
print(s2)
s2=set(s1)
print(s2)
# join two sets
set1={1,2,3}
set2={4,5,6,7}
set3=set1.union(set2)
print(set3)
set1.update(set2)
print(set1)# we can using existing variable we can't use extra variables in the set
#find length of the set
print(len(s))
# is subset()
x={'a','b','c'}
y={'f','a','h','c','k','s'}
z=x.issubset(y)
print(z)
#is subset()
y={'a','b','c'}
x={'f','a','h','c','k','s'}
z=x.issubset(y)
print(z)
#difference()
x={'bmw','benz','ferari'}
y={'bmw','xuv500','eartiga'}
z=x.difference(y)
print(z)
# Intersection()
s={1,2,3,4,'1'}
t={1,'1',4}
z=s.intersection(t)
print(z)
#forezenset
#when a set is converted into forzenset we can say update and remove operations cannot be perforned
s={1,2,3}
print(s)
print(type(s))
#convert a set into frozen set
f=frozenset(s)
print(f)
print(type(f))

f.update([4])# frozen set is immutable
print(f) # error
f.remove(3)
print(f)# error
f.clear()
print(f)# error
#set constructor
myset=set(('hi','hello','byee'))
print(myset)
