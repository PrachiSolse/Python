#Program to Check Prime Number
n=int(input("Enter the number:"))
if n==1:
    print(f"{n} is not a prime number")
elif n==0:
    print("Not a prime number")
elif(n>2):
    for i in range(2,n):
        if(n%i==0):
            print("not a prime")
            break
        else:
            print("prime")
            break