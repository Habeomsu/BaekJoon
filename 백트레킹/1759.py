import sys

L,C = map(int,sys.stdin.readline().split())

arr = list(map(str,sys.stdin.readline().split()))
arr = sorted(arr)

str = []

aeiou = []

for i in arr:
    if i in ('a','e','i','o','u'):
        aeiou.append(i)

def find_pass(start):
    if len(str)==L:
        sum =0
        for i in aeiou:
            sum += str.count(i)
        if sum>=1 and L-sum>=2:
            return print("".join(str))

    for i in range(start,len(arr)):
        str.append(arr[i])
        find_pass(i+1)
        str.pop()

find_pass(0)

