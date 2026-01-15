#Swap two numbers (use temporary variable ).
a=23
b=43
print("a=",a,"b=",b,"before swap" )
temp=a
a=b
b=temp
print("a=",a,"b=",b,"After swap" )


#Swap two numbers (use  without using temporary variable)
a = 2
b = 3
print("a =", a, " b =", b)
a = a + b
b = a - b
a = a - b
print("a =", a, " b =", b)
