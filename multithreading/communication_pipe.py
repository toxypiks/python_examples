from multiprocessing import Process, Pipe

#let two processes talk to each other
def fun(conn):
    conn.send([42,None,'hello'])
    conn.close()


if __name__ == '__main__':
    connection_1, connection_2 = Pipe()
    p = Process(target=fun,args=(connection_2,))
    p.start()
    print(connection_1.recv())
    p.join()
