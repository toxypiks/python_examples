from multiprocessing import Process, Manager


def fun(d, l):
    d[1] = 'one' #adds the value 'one' to dict[1]
    d[2] = 'two' #adds the value 'two' to dict[2]
    l.reverse() #reverses list


if __name__ == '__main__':
    mgr = Manager()
    d = mgr.dict()
    l = mgr.list(['a', 'b', 'c', 'd'])

    p = Process(target=fun, args=(d, l))
    p.start()
    p.join()

    print(d)
    print(l)
