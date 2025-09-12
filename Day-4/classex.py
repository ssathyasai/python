class student:
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
    def display(self):
        print("******Student details*****")
        print("Name:",self.name," RollNo:",self.roll," Marks:",self.marks)
s1=student("sathya",1,100)
s1.display()
s2=student("Sai",2,99)
s2.display()