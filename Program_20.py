# Reverse a number
n=int(input("Enter number: "))
num=n
while num>0:
    last_digit= num%10
    print(last_digit)
    num=num//10
