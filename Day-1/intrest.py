p=int(input("Enter the principle amount:"))
t=int(input("Enter the duration:"))
r=int(input("Enter the rate of intrest:"))
s_i=(p*t*r)//100
in_hand=p+s_i
print("Simple intrest {}".format(s_i))
print("Amount in hand {}".format(in_hand))