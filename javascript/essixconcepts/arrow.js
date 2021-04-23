//var add=(num1,num2)=>num1+num2
//console.log(add(10,30));

var arr=[10,20,30,40,11,12,13,41,42,43]

let min=arr.reduce((num1,num2)=>num1>num2?num2:num1)
console.log(min);

//var squares=arr.map(no=>no**2)
//console.log(squares);

//arr.forEach(num=>console.log(num))

//arr.map((num)=>num**3).forEach(num=>console.log(num))

//arr.filter(num=>num%2==0).forEach(num=>console.log(num))

//arr.sort((no1,no2)=>no1-no2).forEach(num=>console.log(num))

let num=arr.reduce((num1,num2)=>num1+num2)
console.log(num);