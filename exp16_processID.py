import threading
import os

def display_info():
 print(f"Thread Name:{threading.current_thread().name}")
 print(f"Process ID:{os.getpid()}\n")
 
t1=threading.Thread(target=display_info,name="Thread-1")
t2=threading.Thread(target=display_info,name="Thread-2")
t3=threading.Thread(target=display_info,name="Thread-3")
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print("All threads have completed")