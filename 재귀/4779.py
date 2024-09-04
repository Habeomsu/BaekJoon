import sys

def can(n):
    if n==0:
        return '-'
    else:
        return can(n-1)+' '*(3**(n-1))+can(n-1)
while True:
    n=sys.stdin.readline().strip()
    if n=='':
        break
    else:
        print(can(int(n)))