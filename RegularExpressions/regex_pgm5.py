#a,,k first character must be an alphabets b/w a-k
#second must be digit divisible by 3
#followed by any number of character


from re import *
varname=input("enter variable name")

rule="[a-k][369][a-zA-Z0-9]*"

matcher=fullmatch(rule,varname)
if matcher==None:
    print("invalid variable name")
else:
    print("valid variable name")