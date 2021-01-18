limit=int(input("enter limit"))
lst=[2,6,4]
lst=[3,4,5]
lst=list()
for i in range(0,limit):
    number=int(input("enter number"))
    lst.append(number)
out=list()
total=sum(lst)
for num in lst:
    out.append(total-num)
print(out)