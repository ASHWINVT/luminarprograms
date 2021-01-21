lst=[1,2,3,4,5]
low=0
upp=len(lst)-1
pair_list=[]
element=int(input("enter element"))
while(low<upp):
    tot=lst[low]+lst[upp]
    if(element==tot):
        pair_list.append((lst[low],lst[upp]))
        upp=upp-1
    elif(element>tot):
        low+=1
    else:
        upp-=1
print(pair_list)



#for i in range(0,len(lst)):
 #   for j in range(i+1,len(lst)):
  #      if(lst[i]+lst[j]==num):
        #    print(lst[i],lst[j])