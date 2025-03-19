### 두개의 수열이 주어질때 최대 공통 부분 수열은 다이나믹 프로그래밍을 사용하여 계산한다.
### dp[i][j] = dp[i-1][j-1]+1 or max(dp[i-1][j],dp[i][j-1]) 이다...
### 최대 공통 부분 수열이 아니라 그냥 모든 부분 수열을 나열한다 ...
### 디피를 구하되, 숫자가 변경시 배열에 추가해준다 ... -> [0,1,1 1,5,1 5,1 1 5]
#### 디피를 구하되, 확인하는 숫자와 같은 숫자일 경우 현재 들어있는 집합에다가 확인 숫자를 모두 더해준다...
##### 최대길이 수열을 찾는다
##### 그리고 가장 큰 숫자를 찾는다
##### 그리고 그 뒤에 수를 바로 넣어 준다
###### 그리고 그 뒤에부터는 앞에 것과 비교해서 만약에 자신이 더 클 경우 나머지들은 빼준다 ..

### 두 배열을 중복없이 같이 들어있는 수중 가장 큰 수를 뽑는다 .
### 그리고 나서 각 배열의 해당 가장 큰 수 부터 끝까지 또 한다.
### 없을 때 까지 반복한다.

import sys

num1 = int(sys.stdin.readline())
arr1 = list(map(int, sys.stdin.readline().split()))
num2 = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().split()))

final=[]

while True:
    set1=set(arr1)
    set2=set(arr2)

    result = set1 & set2
    if len(result)==0:
        break
    max_num = max(result)
    final.append(max_num)
    index1 = arr1.index(max_num)
    index2 = arr2.index(max_num)
    arr1=arr1[index1+1:]
    arr2=arr2[index2+1:]

if len(final)==0:
    print(0)
else:
    print(len(final))
    print(*final)
