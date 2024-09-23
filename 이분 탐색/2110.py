import sys
n,c=map(int,sys.stdin.readline().split())
arr=[]
for i in range(n):
    arr.append(int(sys.stdin.readline()))
arr=sorted(arr)
start=1
end=arr[-1]-arr[0]
answer=0
def find(start,end,num):
    while start<=end:
        mid = (start+end)//2
        current=arr[0]
        cnt=1

        for i in range(1,len(arr)):
            if arr[i]>= current+mid:
                cnt +=1
                current =arr[i]
        if cnt >= num: # 카운트가 많다 -> 기준 거리가 작다는 뜻
            global answer
            start = mid+1
            answer=mid
        else: # 카운트가 적다 -> 기준 거리가 너무 멀다는 뜻
            end=mid-1
find(start,end,c)
print(answer)



