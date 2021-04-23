class Parent:
    def mobile(self):
        print("nokia5510")
class Child(Parent):
    def mobile(self):
        print("iphone11")



c=Parent()
#c.mobile()
print(c) #print an object while printing object __str__() will invoke object