import sys
n=int(sys.stdin.readline())
for i in range(n):
    a,b=map(int,sys.stdin.readline().split())
    sum=0
    for j in range(a):
        c=sys.stdin.readline().strip('\n')
        count=0
        for i in range(b):
            if c[i]=='.':
                count=0
            else:
                if count==0:
                    sum=sum+1
                    count+=1
                else:
                    count +=1
        print(sum)
    print(sum)