import sys

S=sys.stdin.readline().strip("\n")
T=sys.stdin.readline().strip("\n")
arr=list(T)
for i in range(len(T)-len(S)):
    if arr[-1]=='A':
        arr.pop(-1)
    else:
        arr.pop(-1)
        for i in range(len(arr)//2):
            arr[i],arr[-1-i]=arr[-1-i],arr[i]

result= ''.join(arr)
if result==S:
    print(1)
else:
    print(0)