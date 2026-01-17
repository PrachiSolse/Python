#Count how many vowels are in a string.
word=input("Enter the sentence: ")
vowels="AEIOUaeiou"
count=0
for char in word:
    if char in vowels:
        count+=1
print(count)