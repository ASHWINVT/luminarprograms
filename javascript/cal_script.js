

function dispBox(num){
    var res=document.querySelector(".result")
    res.value+=num

}
function equal(){
    var res=document.querySelector(".result").value
    var out=eval(res)
    res=document.querySelector(".result").value=out

}

function del(){
    var res=document.querySelector(".result").value
    var data=res.slice(0,-1)
    res=document.querySelector(".result").value=data
}