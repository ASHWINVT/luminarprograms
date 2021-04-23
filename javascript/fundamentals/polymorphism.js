class calc{
    add(){
        console.log("onside nomarg method");
    }
    add(num){
        console.log("inside one arg method");
    }
    add(num1,num2){
        console.log("inside two arg method");
    }
}


var cal=new calc()
cal.add(10,20);
cal.add()