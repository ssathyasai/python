def store_students():
    lis = []   
    for i in range(3):
        roll = int(input(f"Enter roll no of student {i+1}: "))
        name = input(f"Enter name of student {i+1}: ")
        marks = int(input(f"Enter marks of student {i+1}: "))
        tup = (roll, name, marks)
        lis.append(tup)   
    return lis

def high_mark():
    students = store_students()      
    high = students[0][2]            
    z = 0                            

    for i in range(1, len(students)):
        if students[i][2] > high:
            high = students[i][2]
            z = i

    print("Name of the student with highest marks:", students[z][1])
    print("Details of the student with marks >77")
    for i in students:
        if(i[2]>77):
            print(i)
    

high_mark()
