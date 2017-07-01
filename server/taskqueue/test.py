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
        q.add("E:\work\创业之路\公司事务\专利申请", action, 2)

    for task in q.finished:
        for tk in q.waiting:
            print(tk.getName())
        # print (q.running)
        # print (q._finished)
        # print (task.result)
        print("one task")
    print (time()-start)


if __name__ == '__main__':
    main()










