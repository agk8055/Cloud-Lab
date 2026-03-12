import threading
import time
def find_square(num):
 print(f"Square of {num}:{num**2}")
def find_cube(num):
 print(f"Cube of {num}:{num**3}")
num=5
start_time=time.time()
t1=threading.Thread(target=find_square,args=(num,))
t2=threading.Thread(target=find_cube,args=(num,))
t1.start()
t2.start()
t1.join()
t2.join()
end_time=time.time()
print(f"Execution time:{end_time-start_time:4f}seconds")