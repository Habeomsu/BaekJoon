import queue
import sys
Q=queue.Queue()
n=int(sys.stdin.readline())
for i in range(n):
    a=sys.stdin.readline().split()
    if a[0] =='push':
        Q.put(a[1])
    elif a[0] == 'pop':
        if Q.empty():
            print(-1)
        else:
            result=Q.get()
            print(result)
    elif a[0] == 'size':
        print(Q.qsize())
    elif a[0] == 'empty':
        if Q.empty():
            print(1)
        else:
            print(0)
    elif a[0] == 'front':
        if Q.empty():
            print(-1)
        else:
            print(Q.queue[0])
    elif a[0] == 'back':
        if Q.empty():
            print(-1)
        else:
            print(Q.queue[-1])