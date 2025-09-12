class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print("***Employee Details***")
        print("Name of the Employee:",self.name,"\nSalary of employee:",self.salary)
class manager(employee):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department=department
    def display(self):
        super().display()
        print("Department of the employee",self.department)
e1=employee("sathya",20000)
e1.display()
m1=manager("sunny",50000,"data science")
m1.display()