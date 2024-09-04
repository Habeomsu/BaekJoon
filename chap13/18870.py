import sys
n = int(input())
arr1=list(map(int,sys.stdin.readline().split()))
M=min(arr1)
for i in range(len(arr1)):
    arr1[i]=arr1[i]-M
S=set(arr1)
arr2 = sorted(list(S))
dic={value:idx for idx,value in enumerate(arr2)}
for i in arr1:
    print(dic[i],end=' ')