# write a pyhton program that accepts 3 numbers from user and calculate average
a,b,c=[int(a) for a in input("enter the three numbers:").split()]
average=(a+b+c)/3 
print("Average is:",average)