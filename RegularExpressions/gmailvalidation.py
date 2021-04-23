from re import *

gmail=input("enter gmail")

rule='[a-zA-Z.]*[/d]*@gmail.com'

matcher=fullmatch(rule,gmail)
if matcher==None:
    print("invalid gmail")
else:
    print("valid gmail")