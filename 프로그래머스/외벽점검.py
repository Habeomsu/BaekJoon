from itertools import permutations


def solution(n, weak, dist):
    answer = -1

    for i in range(len(dist)):
        friends = permutations(dist, i + 1)
        for friend in friends:
            for j in range(len(weak)):
                make_arr = make(weak, n, j)
                if posible(make_arr, friend):
                    answer = i + 1
                    return answer

    return answer


def make(weak, n, idx):
    new_arr = []
    for i in range(idx, len(weak)):
        new_arr.append(weak[i])
    for i in range(idx):
        new_arr.append(weak[i] + n)
    return new_arr


def posible(make_arr, friends):
    result = True
    max_friends = len(friends)
    now = make_arr[0] + friends[0]
    now_idx = 1
    for i in range(1, len(make_arr)):
        if now >= make_arr[i]:
            continue
        else:
            if now_idx >= max_friends:
                result = False
                break
            else:
                now = make_arr[i] + friends[now_idx]
                now_idx = now_idx + 1
    return result


'''


1. dist의 길이가 최대 8이므로 친구 수의 따른 완전탐색을 진행한다.
    1.1 친구수를 기준으로 dist 배열은 모든 경우의 수를 구해주어야한다. 
    1.2 만약 최대 배열을 진행하고 값이 없으면 -1을 반환한다.
2. 취약점 배열을 0번 인덱스 부터 직선으로 표현한다. -> make 함수
    2.1 직선 표현시 시작 인덱스보다 작은 인덱스들은 마지막에 +n 을 해준다.
3. 취약점 점검 가능한 함수를 만든다.
    3.1 현재 거리 + 친구가 이동할 수 있는 거리를 기준으로 잡는다.


'''