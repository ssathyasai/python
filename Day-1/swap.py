a=10
b=20
print("Before Swapping a is {} b is {}".format(a,b))
a=b+a
b=a-b
a=a-b
print("after swaping a is {} b is {}".format(a,b))
t=a
b=a
a=t
print("after swaping using temp a is {} b is {}".format(a,b))