n=int(input())
a=3
answer=0
if n==1:
    a=3
else:
    for i in range(1,n):
        a = 2*a-1
print(a*a)