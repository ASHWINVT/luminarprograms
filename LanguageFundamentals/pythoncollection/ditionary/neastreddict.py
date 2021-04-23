employee={
    1000:{"id":1000,"name":"tom","salary":25000,"exp":1},
    1001:{"id" :1001,"name":"john","salary":30000,"exp":2},
    1002:{"id" :1002,"name":"dani","salary":35000,"exp":2},
    1003:{"id" :1003,"name":"abi","salary":30000,"exp":1},

}

#print(employee[1000])

def print_employee(**kwargs ):#id=None,prop=None):
  #  print(kwargs)
    id=kwargs["id"]
 #   salary=kwargs["prop"]
    if id in employee:
        print(employee[id]["name"])
        if "prop" in kwargs:
            prop=kwargs["prop"]
            print(employee[id][prop])
        else:
            pass
    else:
        print("employee is not exist")
print_employee(id=1000,prop="salary")












#employee who have id=1001
#if 1000 in employee:
#    print(employee[1001]["name"])
#else:
#   print("employee with id not exist")


#salary 1003

#if 1003 in employee:
