class Employees{
    constructor(eid,name,sal,desig){
        this.eid=eid;
        this.name=name;
        this.sal=sal;
        this.desig=desig;
    }
    printDetails=()=>{
        console.log(this.eid+this.name+this.sal+this.desig);
    }
}

var employee=[]
var obj=new Employees(100,"leo",45000,"developer")
var obj1=new Employees(101,"ashleo",35000,"developer")
var obj2=new Employees(102,"ramos",28000,"qa")
var obj3=new Employees(103,"ozil",25000,"qa")
employee.push(obj)
employee.push(obj1)
employee.push(obj2)
employee.push(obj3)
employee.forEach (emp=>console.log(emp.desig))
employee.map(emp=>emp.sal+2000).forEach(sal=>console.log(sal))
employee.map(emp=>emp.name.toUpperCase()).forEach(name=>console.log(name))
employee.filter(emp=>emp.desig="developer").forEach(emp=>console.log(employee))
employee.sort((o1,o2)=>o1.sal>o2.sal?1:-1).forEach(num=>console.log(employee))
const sal=employee.map(obj=>obj.sal).reduce((sal1,sal2)=>sal1>sal2?sal1:sal2)
console.log(sal);