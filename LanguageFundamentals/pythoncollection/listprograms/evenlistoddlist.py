evnlist=list()
oddlist=list()
for num in lst:
    if(num%2==0):
        evnlist.append(num)
    else:
        oddlist.append(num)
print(oddlist)
print(evnlist)
print("oddsum",sum(oddlist))
print("evnsum",sum(evnlist))