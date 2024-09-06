import sys
import heapq
jewel=[]
maxweight=[]
n,m=map(int,sys.stdin.readline().split())
for i in range(n):
    jewel.append(list(map(int,sys.stdin.readline().split())))
for j in range(m):
    c=int(sys.stdin.readline())
    maxweight.append(c)
result=0
maxwieght=sorted(maxweight)
jewel = sorted(jewel)
temp=[]
j=0
for bag in maxwieght:
    while j<n and jewel[j][0]<=bag:
        heapq.heappush(temp,-jewel[j][1])
        j+=1
    if temp:
        result += -heapq.heappop(temp)
print(result)