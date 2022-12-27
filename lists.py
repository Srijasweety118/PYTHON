mylist=['usa','uk','india']
print(mylist)
mylist.append('canada')
print(mylist)

list=[0,1,2,3]
print(list)
print(type(list))
# 
list=[10,20,30,'python',-1,3,4]
print(list)
#indexing
print(list[3])
print(list[-1])
print(list[-3])
#slicing 
list=[10,20,30,'python',-1,3,4]
print(list[0:3])
print(list[0:4])
print(list[::])
print(list[-1:])
print(list[:4])
#passing step value
print(list[:4:2])
print(list[::-1])  #it will display reverse order
print(list[::-3])
# adding elements to list
# we can use append()
list.append(50)
print(list) # it is added in the last in list
# insert()
list.insert(1,60) #where we can mention the position it will be store in place
print(list)
# extend() we can add multiple elements in list
list.extend([1,2,3])
print(list) # it will add end of the list
# removing elements from list
#remove()
list.remove(30)
print(list) 
# pop(),pop(index)
list.pop(5)
print(list)
list.remove('python')
print(list)
# max and min element in the list
print(max(list)) # it will shows large value in the list
print(min(list))
#sort()
list.sort()
print(list)
list.sort(reverse=True) # it will display in descending order
# length of list
print(len(list))
#repetition it will repeats the elements in the list ,it is indicated as *
print(list*2)
# copy a list-copy(),list()
l1=[1,2,3]
print(l1)
l2=l1.copy()
print(l2)
#list concatenation
lst1=[1,2,3]
lst2=[4,5,6]
lst3=lst1+lst2
print(lst3)
print(lst1+[4,5,6])
print([1,2,3]+[4,5,6])
#membership test '-in' and 'not in'
l1=[1,2,'1','hi','heyy']
print(l1)
print(1 in l1)
print(2 not in l1)
print("1" not in l1)
print('hi' not in l1)
print('hi' in l1)
print(1 and 2 and 'hi' in l1)
#nested list- one list inside another
lst=['python',[1,2,3],['a']]
print(lst)
print(lst[2])
print(lst[0])
print(lst[1])
print(lst[0][1])
print(lst[2][0])
print(lst[1][0])
#list constructor-list(())
#mylist=list(('usa','canada','india'))
print(mylist)

# lists  are mutable
mylist=['usa','uk','india']
print(mylist)
mylist[1]='canada'
print(mylist)
mylist.append('germany')
print(mylist)
# count()
l1=[1,2,3,1,1,'1',2,'2']
print(l1.count(1))
print(l1.count(2))
print(l1.count(3))
#index()
print(l1.index("1"))
print(l1.index(3))
print(l1.index('2'))
print(len(l1))
# clear()
l1.clear()                                             
print(l1)

mylst=list((1,2,3))
print(mylst)