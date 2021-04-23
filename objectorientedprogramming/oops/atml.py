class Bank:
    def bal_enq(self):
        print("inside bal enq")
    def withdraw(self):
        print("inside withdraw")
    def __deposit(self):
        print("inside deposit")

class atm(Bank):
    pass
obj=Bank()
obj._Bank__deposit()
#b=Bank()
#b.withdraw()
#b.deposit()