class Book(object):
    def __init__(self,pages):
        self.pages=pages
    def __add__(self, other):
        return Book(self.pages+other.pages)
    def __sub__(self, other):
        return Book(self.pages-other.pages)
    def __mul__(self, other):
        return Book(self.pages*other.pages)
    def __str__(self):
        return str(self.pages)
obj=Book(1000)
obj1=Book(200)
obj2=Book(300)
print(obj+obj1+obj2)
print(obj-obj1-obj2)
print(obj*obj1*obj2)