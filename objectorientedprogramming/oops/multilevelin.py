class Parent:
    def m1(self):
        print("inside parent1")
class Child(Parent):
    def m2(self):
        print("inside child")
class subchild(Child):
    def m3(self):
        print("insdie sub child")
obj=subchild()
obj.m3()
obj.m2()
obj.m1()