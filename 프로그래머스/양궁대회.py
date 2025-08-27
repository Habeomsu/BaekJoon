def solution(n, info):
    able_arr = []
    for i in info:
        able = []
        if i == 0:
            able.append(1)
            able.append(0)
        else:
            able.append(i + 1)
            able.append(0)
        able_arr.append(able)
    first_arr = []
    arr = [0] * 11

    def back(arr, idx, n):

        if idx == 10:
            arr_sum = sum(arr)
            left = n - arr_sum
            if left < 0:
                return
            arr[idx] = n - arr_sum
            first_arr.append(arr[:])
            arr[idx] = 0
            return

        if sum(arr) >= n:
            if sum(arr) == n:
                first_arr.append(arr[:])
            return

        for i in able_arr[idx]:
            arr[idx] = i
            back(arr, idx + 1, n)
            arr[idx] = 0

    back(arr, 0, n)
    idx = 0
    max_score = 0
    for i in range(len(first_arr)):
        score = find_score(first_arr[i], info)
        if score >0 :
            if max_score == score:
                if better(first_arr[idx], first_arr[i]):
                    max_score = score
                    idx = i
            elif max_score < score:
                max_score = score
                idx = i

    if max_score == 0:
        return [-1]
    else:
        return first_arr[idx]

def find_score(lion, peach):
    lion_score = 0
    peach_score = 0
    for i in range(11):
        if lion[i] == 0 and peach[i] == 0:
            continue
        if lion[i] > peach[i]:
            lion_score += 10 - i
        elif lion[i] <= peach[i]:
            peach_score += 10 - i
    return lion_score - peach_score


def better(arr1, arr2):
    for i in range(10, -1, -1):
        if arr1[i] != arr2[i]:
            return arr1[i] < arr2[i]
    return False


'''

1. 백트래킹을 이용하여 가능한 경우를 구해준다.
2. 백트래킹의 종료 조건은 n이다.
    2.1 생성된 배열의 합이 n보다 크거나 같으면 백트레킹을 종료한다.
    2.2 생성된 배열의 합이 n이면 최종적으로 반환한다.
3. 어피치의 점수를 기준으로 해당 인덱스에서 라이언이 가질 수 있는 점수를 모은 배열을 생성해준다.
    3.1 라이언은 어피치보다 1 높거나, 0 인 점수를 가질 수 있다.
4. 생성된 모든 배열을 비교하여 가장 높은 점수를 구한다.
5. 만약 점수가 높은 경우가 없으면 -1을 반환한다.

'''