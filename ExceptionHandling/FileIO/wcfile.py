f=open("demo","r")

dict={}

for line in f:
    words=line.restrip("/n").split(" ")
    for word in words:
        if(word not in dict):
            dict[word]=1
        else:
            dict[word]+=1
for k,v in dict.items():
    print(k,v)
