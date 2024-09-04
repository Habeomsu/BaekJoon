import sys
max = int(input())
q = sys.stdin.readline()
a = int(input())
c=0
arr = q.split()
for i in range(max):
    if a == int(arr[i]):
        c +=1
print(c)

