import sys
while True:
    A = sys.stdin.readline().strip()
    if A =='':
        break;
    else:
        a,b =map(int,A.split())
        print(a+b)