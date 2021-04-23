class swift:
    def drive(self):
        print("driving swift car")

class sonet:
    def drive(self):
        print("driving sonet car")

class person:
    def start(self,car):
        car.drive()

sw=sonet()
p=person()
p.start(sw)


#""""""if it walks like duck and it quacks like a duck,then it must be a duck""""""