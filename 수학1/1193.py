n=int(input())
i=2
k=0
a=1
while a<n:
    a = a+i
    k=k+i-1
    i +=1
if i%2==1:
    print(f'{n-k}/{i-n+k}')
else:
    print(f'{i-n+k}/{n-k}')