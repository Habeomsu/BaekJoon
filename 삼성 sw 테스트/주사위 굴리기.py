import sys

N,M,x,y,K = map(int,sys.stdin.readline().split())
Map = []
for i in range(N):
    Map.append(list(map(int,sys.stdin.readline().split())))
move = list(map(int,sys.stdin.readline().split()))

left = 0
mid = 0
right = 0
top = 0
bottom = 0
other = 0

dx = [0,0,-1,1]
dy = [1,-1,0,0]

for i in move:
    nx,ny = x+dx[i-1],y+dy[i-1]
    if 0<=nx<N and 0<=ny<M:
        if i == 1:
            left,mid,right,other = mid,right,other,left
        elif i == 2:
            left,mid,right,other = other,left,mid,right
        elif i == 3:
            top,mid,bottom,other = other,top,mid,bottom
        elif i == 4:
            top,mid,bottom,other = mid,bottom,other,top

        if Map[nx][ny] == 0:
            Map[nx][ny] = mid
        else:
            mid = Map[nx][ny]
            Map[nx][ny] = 0
        print(other)
        x,y = nx,ny
    else:
        continue


'''

1일 경우  좌로 한칸
2일 경우  우로 한칸
3일 경우  아래로 한칸
4일 경우  위로 한칸



'''
