class student:
    def __init__(self,rol,name,course):
        self.rol=rol
        self.course=course
        self.name=name

    def get_student(self):
        print(self.rol,",",self.course,",",self.name)

obj=student(1001,"leo","django")

print(obj.name)
print(obj.course)
print(obj.rol)