num1=int(input("enter first no"))
num2=int(input("enter second no"))
num3=int(input("enter third no"))
if ((num1>num2)&(num1>num3)):
    print("num1 is highest")
elif((num2>num3)&(num2>num1)):
    print("num2 is highest")
elif((num3>num1)&(num3>num2)):
    print("num3 is highest")
else:
    print("numbers are equal")
