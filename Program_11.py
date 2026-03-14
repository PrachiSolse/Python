#Largest no. in array
arr=list(map(int,input("Enter array: ").split()))
arr.sort()
print("Largest element in array is",arr[-1])