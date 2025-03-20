import sys

n , p = map(int,sys.stdin.readline().split())

arr =[[] for _ in range(7)]
cnt = 0
for i in range(n):
    a,b=map(int,sys.stdin.readline().split())
    if len(arr[a]) ==0:
        arr[a].append(b)
        cnt +=1
    else:
        while arr[a] and arr[a][-1] > b:
            arr[a].pop()
            cnt += 1
        if arr[a] and arr[a][-1]==b:
            continue
        else:
            arr[a].append(b)
            cnt +=1
print(cnt)

