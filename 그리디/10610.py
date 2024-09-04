import sys

n=int(sys.stdin.readline())
num=str(n)
answer=0
sum=0

for i in num:
    sum=sum+int(i)
if '0' not in num:
    print(-1)
elif sum%3 !=0:
    print(-1)
else:
    answer=sorted(num,reverse=True)
    print(*answer,sep='')
