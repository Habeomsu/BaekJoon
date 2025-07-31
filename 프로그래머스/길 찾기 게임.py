import sys

sys.setrecursionlimit(10001)


def solution(nodeinfo):
    answer = []
    ## 인덱스를 이용해서 노드 번호 삽입
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i + 1)

    pre_arr = []
    back_arr = []

    def find_pre(arr):
        new_arr = sorted(arr, key=lambda x: -x[1])
        parrent_node = new_arr[0]

        new_arr = sorted(new_arr, key=lambda x: x[0])
        idx = new_arr.index(parrent_node)
        left_node = new_arr[:idx]
        right_node = new_arr[idx + 1:]

        pre_arr.append(parrent_node[2])
        if left_node:
            find_pre(left_node)
        if right_node:
            find_pre(right_node)

    def find_back(arr):
        new_arr = sorted(arr, key=lambda x: -x[1])
        parrent_node = new_arr[0]

        new_arr = sorted(new_arr, key=lambda x: x[0])
        idx = new_arr.index(parrent_node)
        left_node = new_arr[:idx]
        right_node = new_arr[idx + 1:]
        if left_node:
            find_back(left_node)
        if right_node:
            find_back(right_node)
        back_arr.append(parrent_node[2])

    find_pre(nodeinfo)
    find_back(nodeinfo)

    answer.append(pre_arr)
    answer.append(back_arr)

    return answer


'''

1. 각 노드에 번호를 포함한 새로운 배열을 생성한다.
2. y 값을 내림차순, x 값을 오름 차순으로 배열을 정렬한다.
3. y 값을 기준으로 내림차순 정렬 후 0번째 원소가 부모 노드이다.
4. x 값을 오름 차순 정렬 후 부모노드 보다 x값이 작으면 왼쪽, 부모노드 보다 x 값이 크면 오른쪽이다.
5. 전위 표기는 부모,오른쪽,왼쪽 순으로 재귀를 사용한다.
6. 후위 표기는 오른쪽,왼쪽,부모 순으로 재귀를 사용한다.



'''