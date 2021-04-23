class Students:
    def __init__(self,rol,name,course,total):
        self.rol=rol
        self.name=name
        self.course=course
        self.total=total

    def __str__(self):
        return self.course

obj=Students(100,"leo","django",140)
obj1=Students(102,"messi","Data",145)
obj2=Students(103,"debruyne","django",150)
obj3=Students(104,"ozil","mean",135)

#print(obj)

slist=[]
slist.append(obj)
slist.append(obj1)
slist.append(obj2)
slist.append(obj3)
total=0
for Students in slist:
    if Students.course=="django":
        total+=Students.total
print("total",total)



#total of django students