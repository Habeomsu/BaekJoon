import sys

n=int(sys.stdin.readline())
arr=[]
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))
rgb=[[0]*3 for _ in range(n)]
rgb[0]=arr[0]
for i in range(1,n):
    rgb[i][0] = min(rgb[i-1][1], rgb[i-1][2]) + arr[i][0]
    rgb[i][1] = min(rgb[i - 1][0], rgb[i - 1][2]) + arr[i][1]
    rgb[i][2] = min(rgb[i - 1][0], rgb[i - 1][1]) + arr[i][2]
print(min(rgb[-1]))