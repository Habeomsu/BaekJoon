import sys

G = int(sys.stdin.readline())
P = int(sys.stdin.readline())

arr=[]

arr=list(range(G+1))

def find(x):
    if arr[x] !=x:
        arr[x]=find(arr[x])
    return arr[x]

def union(a,b):
    rootA = find(a)
    rootB = find(b)
    if rootA != rootB:
        arr[rootA]=rootB

count = 0

for _ in range(P):
    g = int(sys.stdin.readline())
    root = find(g)
    if root == 0:
        break
    union(root,root-1)
    count += 1

print(count)