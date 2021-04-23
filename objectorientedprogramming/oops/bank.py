

from datetime import datetime

class Bank:
    bank_name="sbi"
    def create_account(self,acno,name,min_bal):
        self.acno=acno
        self.name=name
        self.bal=min_bal

    def deposit(self,amount):
        self.bal += amount

        print("Your Ac",self.acno,"Has been credited with amount",amount,"on",datetime,"avl balance",self.bal)

    def withdrawal(self,amount):
        if self.bal > amount:
            self.bal -= amount
            print("Your Ac", self.acno, "Has been debited with amount", amount, "on", datetime,"avl balance",self.bal )
        else:
            print("Transaction cancelled with error code")

    def bal_enq(self):
        print(self.bal)


obj=Bank()
obj.create_account(1000,"leo",30000)
obj.withdrawal(10000)

obj2=Bank()
obj2.create_account(1000,"messi",20000)
