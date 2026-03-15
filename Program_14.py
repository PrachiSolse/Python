#Count frequency of each element in an array
from collections import Counter
arr=list(map(int,input("Enter array:").split()))
freq=Counter(arr)
print(arr[4],freq[4])
