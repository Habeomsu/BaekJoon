import sys
n1 = int(input())
arr1= list(map(int,sys.stdin.readline().split()))
n2 = int(input())
arr2=list(map(int,sys.stdin.readline().split()))
dict = {arr2[i]:0 for i in range(n2)}
for i in arr1:
    dict[i]=1
for i in arr2:
    print(dict[i],end=' ')