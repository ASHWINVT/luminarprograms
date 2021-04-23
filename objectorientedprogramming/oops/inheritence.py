class parent:
    def phone(self):
        print("i have mi 7")


class Child (parent):
    pass
num=int("10")
print(type(num))
c=Child()
#c.phone()
print(id(c))