import sys,re
while True:
    a=sys.stdin.readline().strip("\n")
    if a[0]=='.':
        break
    S=[]
    answer=re.sub(r'[a-zA-Z]','',a)
    answer=answer.replace(' ','')
    answer=answer.replace('.','')
    for i in answer:
        if len(S) ==0:
            S.append(i)
        else:
            if S[-1]=='(' and i==')':
                S.pop()
            elif S[-1] == '[' and i==']':
                S.pop()
            else:
                S.append(i)
    if len(S)==0:
        print('yes')
    else:
        print('no')



