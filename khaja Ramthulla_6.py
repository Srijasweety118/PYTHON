
#1.use a set to find the unique values of list :
#mylist = [2,2,2,2,2,2,6,6,6,6,6,3,3,3,3,3,3]
mylist = [2,2,2,2,2,2,6,6,6,6,6,3,3,3,3,3,3]
print(set(mylist)) #output :{2,3,6}
#2
'''2.Given a set,demostrate the use of copy().
   s={"fb","insta","twitter","whatsapp"}''' 
s={"fb","insta","twitter","whatsapp"}
s1=s.copy()
print(s1) #output: {"fb","insta","twitter","whatsapp"}
#3.create set and demonstrate the use of difference(),subset(),superset(),intersection.

s={"fb","insta","twitter","whatsapp"}
s1={'insta','fb','youtube'}
d=s.difference(s1)
print(d) # output:{'watsap','twitter'}

d=s.issubset(s1)
print(d)  # output:false

d=s.issuperset(s1)
print(d) # output : false

d=s.intersection(s1)
print(d) #output:{'fb','insta'}
#4.create a set and convert it into frozenset.

s={"fb","insta","twitter","whatsapp"}
f=frozenset(s)
print(f) # output:frozenset({'insta', 'whatsapp', 'fb', 'twitter'})
#5.show how two sets can be joined with an example.

s={'insta', 'whatsapp', 'fb', 'twitter'}
s1={'python','js','java'}
s2=s.union(s1)
print(s2) # output: {'python', 'js', 'twitter', 'fb', 'whatsapp', 'java', 'insta'}