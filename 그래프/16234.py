import sys
from collections import deque

n,l,r = map(int,sys.stdin.readline().split())

arr=[]

for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(x,y,visit,visit_cnt):
    que=deque()
    que.append((x,y))
    sum = arr[x][y]
    count = 1
    visit[x][y]=visit_cnt
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n and visit[nx][ny]==0:
                if l<=abs(arr[nx][ny]-arr[x][y])<=r:
                    visit[nx][ny]=visit_cnt
                    sum +=arr[nx][ny]
                    count +=1
                    que.append((nx,ny))
    return sum, count # 만약 count == 1 이면 그냥 패스 , visit_cnt 도 증가 x

total = 0

while True:
    visit = [[0]*n for _ in range(n)]
    visit_cnt = 1
    dic ={}
    for i in range(n):
        for j in range(n):
            if visit[i][j]==0:
                sum,count = bfs(i,j,visit,visit_cnt)
                if count != 1:
                    dic[visit_cnt]=sum//count
                visit_cnt +=1
    if not dic:
        break
    for i in range(n):
        for j in range(n):
            if visit[i][j] in dic:
                arr[i][j] = dic[visit[i][j]]
    total +=1

print(total)