var text="hello hai hello hai"
var dict={}
var words=text.split(" ")



for(let word of words)
{
    if(word in dict){
        dict[word]+=1
    }
    else{
        dict[word]=1
    }
}
console.log(dict);