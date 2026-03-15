#Second smallest and second largest
arr=list(set(map(int,input("Enter the Array:").split())))
arr.sort()
print("Second smallest is",arr[1],"and second largest is",arr[-2])
