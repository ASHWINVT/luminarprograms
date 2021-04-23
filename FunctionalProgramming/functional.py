from functools import reduce

add=lambda num1,num2: num1+num2
print(add(30,40))
sub=lambda num1,num2:num1-num2
print(sub(50,40))
cube=lambda num:num**3
print(cube(3))
even=lambda num:num%2==0
print(even(25))


#map function
lst=[1,2,3,4,5,6]
#def square(num):
 #   return num**2

sqlist=list(map(lambda num:num**2,lst))
print(sqlist)

#map
lst=[1,2,3,4,5,6]
numlist=list(map(lambda num: num-1 if num<5 else num+1 if num>5 else num,lst))
print(numlist)


#filter function
lst=[1,2,3,4,5,6]
evens=list(filter(lambda num:num%2!=0,lst))
print(evens)

names=["india","pak","usa","aus","srilanka","sa","auckland","newzland"]
upplist=list(map(lambda name:name.upper(),names))
print(upplist)

names=["india","pak","usa","aus","srilanka","sa","auckland","newzland"]
acountry=list(filter(lambda  name:name[0]=='a',names))
print(acountry)

#reduce funtion

lst=[10,11,12,13,14]
#sum=reduce(lambda no1,no2:no1+no2,lst)
#print(sum)
high=reduce(lambda no1,no2:no1 if no1>no2 else no2,lst)
print(high)
lowest=reduce(lambda no1,no2:no1 if no1<no2 else no2,lst)
print(lowest)


no=[1,2,3,4,5] [2,3,4,5,6,7]
#have to creae a algorithm for this