import threading
import time



def display():
    for i in range(1,10):
        time.sleep(1)
        print("child thread execute")
    print(threading.currentThread().getName())

t=threading.Thread(target=display)
t.start()
begintime=time.time()
t.join()
for i in range(1,10):
    time.sleep(1)
    print("main thread executing")
print(threading.currentThread().getName())

endtime=time.time()
total=endtime-begintime
print("total time taken=",total)