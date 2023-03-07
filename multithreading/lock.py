import threading
import time

test_value = 1

#to ensure two threads use the same value each at a time, use Lock 
def work(l):
    global test_value
    m_lock = threading.Lock()
    for i in range(5):
        with m_lock:
            test_value += 1
            print(threading.current_thread().name ,test_value)
        time.sleep(3)

        
l = threading.Lock()

t1 = threading.Thread(target=work, args=(l,))
t1.start()

t2 = threading.Thread(target=work, args=(l,))
t2.start()

t1.join()
t2.join()

        
