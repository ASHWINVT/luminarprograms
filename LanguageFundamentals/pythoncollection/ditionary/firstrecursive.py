pattern="ABABBACEEEEEE"
#find first recursive character A
dict={}
for ch in pattern:
    if ch not in dict:
        dict[ch]=1
    else:
        dict[ch]+=1
       # print(ch,"recursive character")
        #break
for k,v in dict.items():
    print(k,",",v)

print(dict)
data=sorted(dict,key=dict.get,reverse=True)
print(data[0])