import sys
N,M = map(int,sys.stdin.readline().split())
dic1={}
dic2={}
for i in range(N):
    a=sys.stdin.readline().strip('\n')
    dic1[str(i+1)]=a
    dic2[a]=str(i+1)
for j in range(M):
    b=sys.stdin.readline().strip('\n')
    if b in dic1:
        print(dic1[b])
    else:
        print(dic2[b])