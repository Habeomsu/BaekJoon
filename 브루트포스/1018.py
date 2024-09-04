import sys
a, b = map(int,input().split())
sum=0
arr=[]
arr1=['BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB']
arr2=['WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW','WBWBWBWB','BWBWBWBW']
for i in range(a):
    arr.append(list(sys.stdin.readline().replace('\n','')))
for j in range(a-7):
    for k in range(b-7):
        arr[j][k]

