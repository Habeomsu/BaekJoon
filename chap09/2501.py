n=0
answer=0
a, b = map(int,input().split())
for i in range(1,a+1):
    if a%i == 0:
        n=n+1
        if n==b:
            answer=i
print(answer)