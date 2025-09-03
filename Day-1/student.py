stu_num=int(input("Enter the student number"))
stu_name=input("Enter Name of the student:")
s_1,s_2,s_3=map(int,input("Enter subject 1 marks").split(","))
total=s_1+s_2+s_3
avg=total//3
print("Average of student :{}".format(avg))
