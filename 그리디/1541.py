import sys,re
a = sys.stdin.readline().strip('\n')
answer=''
b=a.split('-')
c=[]
for i in range(len(b)):
    if '+' in b[i]:
        c.append(sum(list(map(int,b[i].split('+')))))
    else:
        c.append(int(b[i]))
result=c[0]
for i in range(1,len(c)):
    result=result-c[i]
print(result)