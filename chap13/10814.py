import sys
n = int(input())
arr=[]
for i in range(n):
    a,b=sys.stdin.readline().split()
    arr.append([int(a),b.replace('\n',''),i])
arr = sorted(arr,key=lambda x:(x[0],x[2]))
for i in range(n):
    print(arr[i][0],arr[i][1])