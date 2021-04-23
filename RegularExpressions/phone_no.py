from re import *

phno=input("enter ph no")

rule='(91)?\d{10}'

matcher=fullmatch(rule,phno)
if matcher==None:
    print("invalid phno")
else:
    print("valid phno")