size=int(input("enter size of stack"))

top=0
stk=[]
n=1
def push():
    item =int(input("enter item"))
    global top
    top+=1
    if (top==-1) |(top<size):
        stk.insert(top,item)
    else:
        print("stack overflow")
def pop():
    global top
    top-=1
    if top<0:
        print("stack is empty")
    else:
        print(stk[top],"popped out")
    #print("item poped out")
def disp():
    for i in range(0,top):
        print(stk[i])
    print("display")
while(n!=0):
    option=int(input("enter operation 1=>push 2=>pop 3=>disp"))
    if option==1:
        push()
    elif option==2:
        pop()
    elif option==3:
        disp()
    n=int(input("do you want to continue press 0 for exit "))