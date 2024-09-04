import sys
n = int(sys.stdin.readline())
s={}
for i in range(n):
    key,value = sys.stdin.readline().split()
    s[key]=value
arr = sorted(s,reverse=True)
for i in arr:
    if s[i] == "enter":
        print(i)