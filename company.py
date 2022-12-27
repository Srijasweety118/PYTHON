code=int(input("enter the code"))
name=input("enter the name")
desc=input("enter the desc")
company=input("enter the company name")
salary=int(input("enter the salary"))
ta=salary*3/100
da=salary*4/100
hra=salary*5/100
allowance=ta+da+hra
pf=salary*2/100
it=salary*4/100
esi=salary*7/100
deducation=pf+it+esi
gross=salary+ta+da+hra
nett=gross-pf-it-esi

print('code\t name\t desc\t comapany\t salary\t gross\t deducation\t allowance\t nett\t ')
print(code,'\t',name,'\t',desc,'\t',company,'\t',salary,'\t',gross,',\t',allowance,'\t',deducation,'\t',nett)





