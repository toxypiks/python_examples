from threading import Thread
import time


def gui():
    for i in range(10):
        print('#')
        time.sleep(1)

        
def work(how_long):
    time.sleep(how_long)

    
t1 = Thread(target=gui, name='MyCoolGui', args=())
t1.start()


t2 = Thread(target=work, name='MyCoolWorkFunc', args=(2,))
t2.start()

t1.join()
t2.join()
