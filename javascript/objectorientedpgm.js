class Person{
   // setPerson(age,name)
   constructor(age,name){
        this.age=age;
        this.name=name;
    }
    printPerson(){
        console.log(this.age+ ","+this.name);
    }
}

var obj=new Person()
//obj.setPerson(25,"leo")
obj.printPerson()