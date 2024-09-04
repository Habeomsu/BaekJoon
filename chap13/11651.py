import sys
n = int(input())
arr=[]
for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    arr.append([b,a])
arr= sorted(arr)
for j in range(n):
    print(*arr[j][::-1])