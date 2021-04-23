#validate vechicle regno
#kl 2digit 2alphabets 4digits

from re import *

regno=input("enter reg no")

rule='kl\d{2}[a-zA-Z]{2}d\{4}'

matcher=fullmatch(rule,regno)
if matcher==None:
    print("invalid regno")
else:
    print("valid regno")