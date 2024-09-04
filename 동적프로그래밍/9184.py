import sys

def w(a,b,c):
    global arr
    if a<=0 or b<=0 or c<=0:
        return arr[0][0][0]
    elif a>20 or b>20 or c>20:
        return w(20,20,20)
    elif a==b and b==c:
        return arr[a][b][c]
    if arr[a][b][c] != 0:
        return arr[a][b][c]
    elif a<b and b<c:
        arr[a][b][c]= w(a,b,c-1)+w(a,b-1,c-1)-w(a,b-1,c)
    else:
        arr[a][b][c]= w(a-1,b,c)+w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1)
    return arr[a][b][c]

arr=[[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]
arr[0][0][0]=1
for i in range(1,21):
    arr[i][i][i]=2**i

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a==-1 and b==-1 and c==-1:
        break
    else:
        print(f'w({a}, {b}, {c}) = {w(a,b,c)}')