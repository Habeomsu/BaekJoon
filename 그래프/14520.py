import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
arr=[]
for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))
dx=[0,0,-1,1]
dy=[-1,1,0,0]

def bfs(x,y):
    q=deque()
    q.append((x,y))

