from re import *

pattern="[a-z]"

matcher=finditer(pattern,"abc _7Zk@c")
cnt=0
for match in matcher:
    print(match.start())
    print(match.group())