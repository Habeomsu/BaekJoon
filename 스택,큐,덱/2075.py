import sys
import heapq

n= int(sys.stdin.readline())

real = []



arr=[]
for i in range(n):
    nums = list(map(int,sys.stdin.readline().split()))
    if len(arr)==0:
        for num in nums:
            heapq.heappush(arr,num)
    else:
        for num in nums:
            if num>arr[0]:
                heapq.heappush(arr,num)
                heapq.heappop(arr)

print(arr[0])