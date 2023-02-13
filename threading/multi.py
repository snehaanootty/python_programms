import time
import threading

def cal_sqre(num):
    print("calculate the square root of the given number")
    for n in num:
        time.sleep(0.3)
        print("sqaure is :",n * n)
def cal_cube(num):
    print("calculate cube of the given number")
    for n in num:
        time.sleep(0.3)
        print("cube is :",n * n * n)
arr=[4,5,6,7]  #given array of list
t1=time.time() #get total time to execute the functions
# cal_cube(arr)
# cal_sqre(arr)
th1=threading.Thread(target=cal_sqre,args=(arr,))
th2=threading.Thread(target=cal_cube,args=(arr,))
th1.start()
th2.start()
th1.join()
th2.join()
print("total time taken by thrads is:",time.time()-t1)
