# Count number of digits in Integer
#num=int(input("Enter Number: "))
#count=0
#while num>0:
 #   count+=1
  #  num=num//10
#print(count)


#Logarithmic Based approach
from math import log10
def count(num):
    if num == 0:
        return 1
    num = abs(num)
    return int(log10(num) + 1)
# Now this will work perfectly
print(count(867))   # Output: 3
print(count(-50))   # Output: 2
print(count(0))     # Output: 1
