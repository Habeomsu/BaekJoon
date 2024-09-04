n = int(input())
answer=''
for i in range(n):
    m,s = input().split()
    m=int(m)
    for i in s:
        answer += i*m
    print(answer)
    answer=''

