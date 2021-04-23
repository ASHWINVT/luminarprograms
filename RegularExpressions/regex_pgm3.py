from re import *
#pattern="a+" #any no of a excluding 0 number
#pattern="a*" #any no of a including 0 number
pattern="a?"
matcher=finditer(pattern,"aaaaabaabaabaa")
for match in matcher:
    print(match.start(),"=>",match.group())