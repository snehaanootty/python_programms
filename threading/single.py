# """threading"""
#
from time import sleep
from threading import Thread
def task():
    sleep(3)
    print("this is from another thread")
task()

# from threading import Thread
th=Thread(target=task)
th.start()

"""passing arguments"""
from time import sleep
from threading import Thread
def task(sleep_time,message):
    sleep(sleep_time)
    print(message)
th=Thread(target=task,args=(1.5,"this is from  thread"))
th.start()
print("waiting for the thread")
th.join()