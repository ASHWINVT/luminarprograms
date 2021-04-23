#print employee details whose designatio=developer

#no.of employees as developer


class Employee:
    def __init__(self,eid,name,desig,exp,sal):
        self.eid=eid
        self.name=name
        self.desig=desig
        self.exp=exp
        self.salary=sal
    def __str__(self):
        return self.name

f=open("employees","r")
emplist=[]
sallist=[]
for lines in f:
    eid,name,desig,exp,sal=lines.rstrip("\n").split(",")
    emplist.append(Employee(eid,name,desig,exp,sal))


#for Employee in emplist:
 #   sallist.append(Employee.salary)
#print(max(sal))


#print employee details whose designatio=developer

develop=list(filter(lambda emp:emp.desig=="developer",emplist))
for emp in develop:
    print(emp)

#no of emplouyees as developer

develop=list(filter(lambda emp:emp.desig=="developer",emplist))
cnt=len(list(filter(lambda emp:emp.desig=="developer",emplist)))
print(cnt)

#print employees details who have highest salary

maxsal=max(list(map(lambda emp:emp.salary,emplist)))
print(maxsal)