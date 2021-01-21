expenses={"jan":30000,"feb":25000,"march":28000}
print(expenses["march"])
#print("june20" in expenses)
#stored in dict in the form of key value pair
#possible to store duplicate key,key must be unique



expenses["june20"]=25000
print(expenses)

expenses["march"]-=4000
print(expenses["march"])