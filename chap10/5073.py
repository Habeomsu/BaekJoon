while True:
    arr = list(map(int,input().split()))
    Max = max(arr)
    if sum(arr) == 0:
        break;
    else:
        if Max >= (sum(arr)-Max):
            print("Invalid")
        else:
            if arr[0]==arr[1] ==arr[2]:
                print("Equilateral")
            elif arr[0] == arr[1] or arr[1]==arr[2] or arr[0] == arr[2]:
                print("Isosceles")
            else:
                print("Scalene")