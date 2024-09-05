import heapq
import sys
n = int(sys.stdin.readline())
for i in range(n):
    m= int(sys.stdin.readline())
    arr=list(map(int,sys.stdin.readline().split()))
    heapq.heapify(arr)
    result=0
    while len(arr)!=1:
        a=heapq.heappop(arr)
        b=heapq.heappop(arr)
        result +=(a+b)
        heapq.heappush(arr,a+b)
    print(result)

