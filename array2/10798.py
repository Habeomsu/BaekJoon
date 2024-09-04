arr=[0]*5
answer=''
for i in range(5):
    arr[i] = input()
a,b,c,d,e = len(arr[0]),len(arr[1]),len(arr[2]),len(arr[3]),len(arr[4])
M= max(a,b,c,d,e)
for i in range(5):
    if len(arr[i])<M:
        arr[i] =arr[i]+'*'*(M-len(arr[i]))
for i in range(M):
    answer = answer+arr[0][i]+arr[1][i]+arr[2][i]+arr[3][i]+arr[4][i]
print(answer.replace('*',''))







