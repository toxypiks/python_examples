from threading import Thread, Event
import time


def gui(e):
    while not e.is_set():
        e.wait(1)
        print('#')
        time.sleep(1)

#work function calls e.set() to terminate gui function by given time  

def work(how_long, e):
    time.sleep(how_long)
    e.set()


e = Event()


t1 = Thread(target=gui, name='MyCoolGui', args=(e,))
t1.start()


t2 = Thread(target=work, name='MyCoolWorkFunc', args=(2, e))
t2.start()

t1.join()
t2.join()
