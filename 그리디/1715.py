import sys
from queue import PriorityQueue
Q=PriorityQueue()
n=int(sys.stdin.readline())
for i in range(n):
    a=int(sys.stdin.readline())
    Q.put(a)
result =0
for i in range(n-1):
    a=Q.get()
    b=Q.get()
    result+=a+b
    Q.put(a+b)
print(result)