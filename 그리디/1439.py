import sys

q=list(map(int,sys.stdin.readline().strip("\n")))
p=q[:]
sum1=0
sum2=0
cnt1=q.count(1)
cnt0=q.count(0)
result1=0
result2=0
if cnt1 == len(q) or cnt0 == len(q):
    print(0)
else:
    for i in range(len(q)):
        if q[i]==1:
            q[i]=0
            if sum1==0:
                result1+=1
                sum1+=1
        else:
            sum1=0

    for j in range(len(q)):
        if p[j]==0:
            p[j]=1
            if sum2==0:
                result2 +=1
                sum2+=1
        else:
            sum2=0

    if result1<=result2:
        print(result1)
    else:
        print(result2)