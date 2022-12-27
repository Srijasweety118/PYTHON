#1
import pandas as pd
data = {
    'A':['A1', 'A2', 'A3', 'A4', 'A5'], 
    'B':['B1', 'B2', 'B3', 'B4', 'B4'], 
    'C':['C1', 'C2', 'C3', 'C3', 'C3'], 
    'D':['D1', 'D2', 'D2', 'D2', 'D2'], 
    'E':['E1', 'E1', 'E1', 'E1', 'E1'] }
df=pd.DataFrame(data)
df.B.unique()
df.iloc[2]
df.rename(columns={'B':'new_B'})
df.drop_duplicates()
df.loc[2]

# #3.
nums=[7,2,31,5,4,6,8,9]
count=0
while count<7:
    print(nums[count])
    count+=1
    if nums[count]==4:
        continue
    print("End")
# #4.
nums=[7,2,3,1,5,4,6,8,9]
count=0
while count<7:
    print(nums[count])
    count+=1
    if nums[count]==4:
        break
    print("End")
# #5
# if a =[1,2,3]
# a.append([4,5])

#6.
li=[[1,2],[3,4,5]]
print(len(li))
#7.
li={[1,2,3],[4,5,6]}
print([li for x in li for i in x])