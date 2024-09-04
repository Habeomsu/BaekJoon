import sys
import heapq

arr=[]

n=int(sys.stdin.readline())
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))
arr.sort(key=lambda x : (x[0],x[1]))
heap=[arr[0][1]]
for i in range(1,n):
    if heap[0]<=arr[i][0]:
        heapq.heappop(heap)
    heapq.heappush(heap,arr[i][1])
print(len(heap))
