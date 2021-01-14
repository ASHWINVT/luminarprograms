num=input("enter number")
data=""
res=0
for i in range(1,(int(num)+1)):
    data=num*i
    res=res+int(data)
print(res)