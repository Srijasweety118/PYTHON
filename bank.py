

Ac_number=int(input("enter the ac number"))
cust_name=input("enter the cust name")
branch=input("enter the branch name")
ifsc=str("SNB0003536")
address=input("enter the address")
phone=int(input("enetr the phone number"))
deposit=int(input("enter the deposit"))
pan=str("LNWPS1950H")
email=str("SKKHAJARAMTHULLAKHAJA@GMAIL.COM")
min_balance=5000
amount=10000
withdraw=8000
deposit=min_balance+amount
withdraw=amount-withdraw

print("Ac_number \t cust_name")
print(Ac_number,'\t',cust_name)
print("branch \t ifsc")
print(branch,'\t',ifsc)
print("address \t phone") 
print(address,'\t',phone)
print("deposit \t pan ")
print(deposit,'\t',pan)
print("email \t amount")
print(email,'\t',amount)
print(" deposit \t withdraw")
print(deposit,'\n',withdraw)
