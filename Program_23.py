#  Find the Factorial of a Number
num=int(input("Enter the number:"))
factorial=1
if num<0:
    print("Factorial doesn't Exist for negative number")
elif num==0:
    print("1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print(factorial)
