def verify_res(total):
    if(total>=40):
        print("Passed in the exams")
        if(total<50):
            print("student secured Grade C")
        elif(total>51 or total<=70):
            print("Student secured Grade B")
        elif(total>71 or total<=80):
            print("Student secured Grade A")
        else:
            print("Student secured Distinction")
    else:
        print("Failed in the Examination")

stu_num=int(input("Enter the student number:"))
stu_name=input("Enter Name of the student:")
s_1,s_2,s_3=map(int,input("Enter subjects marks Out of 30:").split(","))
total=s_1+s_2+s_3
avg=total//3
print("Name of the student {}".format(stu_name))
print("Student Number {}".format(stu_num))
print("Average of student {}".format(avg))
print("Total marks secured {}".format(total))
verify_res(total)