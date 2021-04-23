var clk=document.querySelector("#clk")

clk.addEventListener("Click",()=>{
    clk.textContent="Clicked";
    clk.style.color="red";
})

var dbl=document.querySelector("#dbl")

dbl.addEventListener("dblclick",()=>{
    dbl.textContent="Double clicked";
    dbl.style.color="green";
})

var ove=document.querySelector("#ove")

ove.addEventListener("mouseover",()=>{
    ove.textContent="Double clicked";
    ove.style.color="blue";
})