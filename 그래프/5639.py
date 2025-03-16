### 전위 순회는 dfs 이다
### 트리를 완성한다 조건, 왼쪽은 부모보다 무조건 작다. 오른쪽은 부모보다 무조건 크다
### 전위를 입력받아 후위로 변환하는 작업 ...
### 부모, 왼쪽, 오른쪽으로 나누는 작업을 한다
### 후위는 왼쪽, 오른쪽, 루트를 출력하는 작업이니 왼쪽 재귀, 오른쪽 재귀, 루트 프린트를 한다.
### 재귀의 조건이 필요하다 -> 노드가 없으면 끝내야한다 ... 즉 시작값이 끝값과 같거나 크다면 종료

import sys

arr = []

while True:
    try:
        a=int(input())
    except:
        break
    arr.append(a)


def preOrder(start,end):

    if start>end:
        return

    b = arr[start]
    index=end+1
    for i in range(start+1,end+1):
        if b<arr[i]:
            index=i
            break
    preOrder(start+1,index-1)
    preOrder(index,end)
    print(b)

preOrder(0,len(arr)-1)
