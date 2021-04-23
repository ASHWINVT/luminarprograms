students={
    1000:{"name":"ajay","course":"mca","total":150},
    1002:{"name":"tom","course":"mca","total":250},
    1003:{"name":"john","course":"mca","total":350},
    1004:{"name":"tomi","course":"mca","total":150},
}

f=open("students")
students={}
for lines in f:
    id,"name","total","course"+lines.rstrip("\n").split(",")

    if id not in students:
        students[id]={"id":id,"name":"name","total":"total","course":"course"}
print(students)








#students={
 #   1000:{"roll":1000,"name":"tom","total":25000,"course":"bca"},
  #  1001:{"roll" :1001,"name":"john","total":30000,"course":"mca"},
  #  1002:{"roll" :1002,"name":"dani","total":35000,"course":"bca"},
   # 1003:{"roll" :1003,"name":"abi","total":30000,"course":"mca"},
#}

#print(students[1000])
def print_data(**kwargs):
    roll=kwargs["roll"]
    if roll in students:
        print(students[roll]["name"])
        if "prop" in kwargs:
            prop=kwargs["prop"]
            print(students[roll][prop])
        else:
            pass
    else:
        print("student not exist")
print_data(roll="1000",prop="course")
