var number=17;
 var flag=0;
 for(let i=2;i<number;i++)
 {
     if(number%i==0)
     {
         flag+=1;
         break;
     }
     else
     {
         flag=0;
     }
 }
if(flag==0)
{
    console.log("prime");
}
else{
    console.log("not prime");
}