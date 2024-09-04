import sys

def rec(s,l,r,sum):
    if l>=r:
        return 1,sum
    elif s[l] != s[r]:
        return 0,sum
    else:
        return rec(s,l+1,r-1,sum+1)

def is_pal(s):
    return rec(s,0,len(s)-1,1)
n=int(sys.stdin.readline())
for i in range(n):
    s=sys.stdin.readline().strip("\n")
    a,b=is_pal(s)
    print(a,b)