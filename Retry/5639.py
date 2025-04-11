import sys
sys.setrecursionlimit(10000000)
arr = []

while True:

    a = input()
    if a == "":
        break
    else:
        arr.append(int(a))

def find(start,end):

    if start > end:
        return

    node = start
    end_start = end+1
    for i in range(start+1,end+1):
        if arr[i] > arr[node]:
            end_start = i
            break
    find(node+1,end_start-1)
    find(end_start,end)
    print(arr[node])
    return

find(0,len(arr)-1)