import taskqueue
from time import time, sleep

def action(n):
    print (".")
    sleep(n)
    return True

def main():
    start = time()
    q = taskqueue.Queue(workers=2)
    
    print ("testing 10 tasks that sleep for 2 seconds each")
    print ("this should take over 20 seconds total")
    print ("will probably take half with taskqueue")
    print (q.num_workers)
    for i in range(10):
        sleep(1)
        q.add(action, 2)

    # print(q.cancelTask(action, 2))

    q.printWaiting()
    
    for task in q.finished:
        print (task.result)
    print (time()-start)


if __name__ == '__main__':
    main()










