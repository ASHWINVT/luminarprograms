

#method overloading

class Maths:
    def add(self):
        print("inside no arg")

    def add(self,num1):
        print("onside one arg")

    def add(self,num1,num2):
        print("inside two arg")

m=Maths()
m.add(10,20)

#method overriding