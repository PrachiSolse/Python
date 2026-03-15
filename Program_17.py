#Program to Check Leap Year
n=int(input("Enter the year:"))
if(n%400==0) and (n%100==0):
    print("Leap Year")
elif(n%4==0) and (n%100!=0):
    print("Leap year")
else:
    print("Not Leap Year")
    