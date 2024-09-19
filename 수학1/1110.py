import sys

n=int(sys.stdin.readline())
if n<10:
    n="0"+str(n)
else:
    n=str(n)
result=0
initial=n
while True:
    m=str(int(n[0])+int(n[1]))
    m=n[1]+m[-1]
    result+=1
    if m ==initial:
        break
    else:
        n=m
print(result)