class employee:
    def __init__(self,id,name,designation,salary):
        self.id=id
        self.designation=designation
        self.name=name
        self.salary=salary
    def print_employee(self):
        print(self.id,",",self.designation,",",self.name,",",self.salary)

obj=employee(1001,"leo","hr",25000)
#obj.set_employee(1001,"leo","hr",25000)
obj.print_employee()
#print(obj.id)
#print(obj.name)
#print(obj.designation)
#print(obj.salary)




