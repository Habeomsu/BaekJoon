import sys
n=int(sys.stdin.readline())
for i in range(n):
    S=[]
    answer=sys.stdin.readline().strip('\n')
    for i in answer:
        if len(S)==0:
            S.append(i)
        else:
            if S[-1]=='(' and i==')':
                S.pop()
            else:
                S.append(i)
    if len(S)==0:
        print('YES')
    else:
        print('NO')