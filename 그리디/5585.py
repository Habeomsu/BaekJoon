import sys
n=int(sys.stdin.readline())
arr=[500,100,50,10,5,1]
result=0
sum=1000-n
i=0
while sum > 0:
    if sum>=arr[i]:
        result =result + sum//arr[i]
        sum = sum%arr[i]
    i=i+1
print(result)
