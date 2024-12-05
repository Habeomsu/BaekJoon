import sys
import heapq

n,m=map(int,sys.stdin.readline().split())

arr= list(map(int,sys.stdin.readline().split()))
heapq.heapify(arr)
for i in range(m):
    a1=heapq.heappop(arr)
    a2=heapq.heappop(arr)
    a3=a1+a2
    heapq.heappush(arr,a3)
    heapq.heappush(arr,a3)

print(sum(arr))

