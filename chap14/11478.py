import sys
answer=sys.stdin.readline().strip('\n')
n=len(answer)
a=0
S=set()
arr=list(answer)
while a<n:
    for i in range(n-a):
        S.add(answer[i:i+1+a])
    a+=1
print(len(S))