import sys

n = int(sys.stdin.readline())

arr = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(n)]

def find(arr,num):
    if num == 2:
        new_arr = []
        for i in range(2):
            for j in range(2):
                new_arr.append(arr[i][j])
        new_arr = sorted(new_arr,reverse=True)
        return new_arr[1]
    else:
        arr1 = [row[:num//2] for row in arr[:num//2]]
        arr2 = [row[num//2:] for row in arr[:num//2]]
        arr3 = [row[:num//2] for row in arr[num//2:]]
        arr4 = [row[num//2:] for row in arr[num//2:]]
        a = find(arr1,num//2)
        b = find(arr2,num//2)
        c = find(arr3,num//2)
        d = find(arr4,num//2)
        new = [a,b,c,d]
        new = sorted(new,reverse=True)
        return new[1]

print(find(arr,n))