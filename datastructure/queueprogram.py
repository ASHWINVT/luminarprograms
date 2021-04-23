size=int(input("enter size of queue"))

front=0
rear=0
que=[]
n=1
def insert():
    item =int(input("enter item"))
    global rear
    if (rear>size):
        print("queue is full")
    else:
        rear+=1
        que.insert(rear, item)
def deletion():
    global front
    if front==rear:
        print("queue is empty")
    else:
        front+=1
        print(que[front])
    #print("item poped out")
def disp():
    for i in range(0,rear):
        print(que[i])
    print("display")
while(n!=0):
    option=int(input("enter operation 1=>insert 2=>delete 3=>disp"))
    if option==1:
        insert()
    elif option==2:
        deletion()
    elif option==3:
        disp()
    n=int(input("do you want to continue press 0 for exit "))