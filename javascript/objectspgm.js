var employee={
    id:1000,name:"ash",desig:"develop",salary:25000
}
//key
//console.log(employee["name"]);

console.log(employee.name);

//chking for gender in there
//console.log("gender" in employee);

employee["gender"]=["male"]

console.log(employee);

for(let key in employee){
    console.log(key);
}