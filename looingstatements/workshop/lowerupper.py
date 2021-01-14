num=int(input("enter number"))
low=int(input("enter low"))
upper=int(input("enter upper"))
for i in range(1,(upper+1)):
    if i**num in range(low,upper):
        print(i**num)
    else:
        pass