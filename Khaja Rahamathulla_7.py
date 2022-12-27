  
d1={'name':"John",'age':30,'city':"delhi",'country':"India"}
#1
d2=d1.copy()
print(d1)
#2
print(d1)
#3
print(len(d1))# 4
#4
d1.pop('city')
print(d1)
#5
d1.clear()
print(d1) # {}


#2.using keys and indexing,print 'python; from the dictionaries:

#d1={'key':'python'}
#d2={'key1':{'key2':'python'}}
#d3={'key1' : [{'nest_key':["let's learn",['python']]}]}
d1={'key':'python'}
d2={'key1':{'key2':'python'}}
print(d1['key'])

d3={'key1' : [{'nest_key':["let's learn",['python']]}]}
print(d3['key1'])
#thisdict = {"emp_name": "Rahul","emp_id": "AA11","emp_salary": 10000}  
# ​3.Given the dictionary change empid to "AA22"

thisdict = {"emp_name": "Rahul","emp_id": "AA11","emp_salary": 10000} 
thisdict['emp_id']='AA22'
print(thisdict)# output:{'emp_name': 'Rahul', 'emp_id': 'AA22', 'emp_salary': 10000}


#4.Refering dictionary in question 3 add an item to this dict dictionary, and also delete the same item added to the dictionary.
# '''1.Demonstrate the following functions for dictionaries:
#    d1={'name':"John",'age':30,'city':"delhi",'country':"India"}
#   1.copy
#   2.dictionary constructor
#   3.length of dictionary
#   4.remove item from the dictionary
#   5.delete dictionary'''

mydict={'name': 'John', 'age': 30, 'city': 'delhi', 'country': 'India'}
mydict['qualification']='betch'
print(mydict)

mydict['designation']='Software developer'
print(mydict)

mydict['salary']='5LPA'
print(mydict)

mydict.pop('qualification')
print(mydict)

mydict.pop('designation')
print(mydict)
mydict.pop('salary')
print(mydict)
