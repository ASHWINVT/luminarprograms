lst=[10,20,30]
#pos=int(input("enter the position to print"))
num1=int(input("num1"))
num2=int(input("num2"))
try:
    res=num1/num2
    print(res)
except:
    num2=int(input("num2"))
    try:
        res=num1/num2
        print(res)
    except:
        num2 = int(input("num2"))
        res = num1 / num2
        print(res)

finally:
    print("i hv a db")
    print("i hv file op")