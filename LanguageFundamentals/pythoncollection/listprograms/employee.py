employees=[
    [10,"christy","data",50000],
    [11, "jhon", "ba", 30000],
    [12, "sab", "data", 40000],
    [13, "tom", "developer", 40000],
    [14,"jhoni","data",30000],
   [15, "sabir", "ba", 50000],
    [16, "tomis", "data", 40000],
    [17, "tammy", "developer", 47000],
    [18, "alex", "developer", 32000],

]

#salary_list=[]
#for emp in employees:
 #   salary_list.append(emp[3])
#high_salary=max(salary_list)
#print(high_salary)

#for emp in employees:
 #   if emp[3]==high_salary:
  #      print(emp)

#print employee name who recievs lowest salary whose designation =developer
d_salary_list=[]
for emp in employees:
    if (emp[2]=="developer"):
        d_salary_list.append(emp[3])



low_sal=min(d_salary_list)
for emp in employees:
    if (emp[3]==low_sal):
        print(emp)

#salary_list=[]
#for emp in employees:
 #   salary_list.append(emp[3])


#low_sal=min(salary_list)
#for emp in employees:
   #if (emp[2]==low_sal):
    #        print(emp)





#group by designation

#d_cnt,da_count,ba_count=0,0,0
#for emp in employees:
 #   if emp[2]=="data":
  #      d_cnt+=1
   # elif emp[2]=="ba":
    #    ba_count+=1
    #else:
     #   da_count+=1
#print("data",da_count,"ba count",ba_count,"developer",d_cnt)









#print number of eemployees in this company

#number_of_employees=len(employees)
#print("no of employees =",number_of_employees)



#how much salary company has to raise in month

#total_amount=0
#for emp in employees:
 #   total_amount+=emp[3]
#print("total amount",total_amount)