import multiprocessing as mp
import time
import os


def test_it():
    print("test_it", os.getpid())
    time.sleep(10)


if __name__ == '__main__':
    print("main", os.getpid())
    p = mp.Process(target=test_it)
    p.start()
    time.sleep(1)
    p.terminate()
    print("is test_it alive? ", p.is_alive())
    time.sleep(1)
    print("is test_it alive? ", p.is_alive())
    p.join()
    print(p.exitcode)
