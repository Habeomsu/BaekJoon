def solution(a):
    answer = 2

    n = len(a)

    if n <= 2:
        return n

    left_min = [0] * n
    right_min = [0] * n

    left_min[0] = a[0]
    right_min[-1] = a[-1]

    for i in range(1, n):
        left_min[i] = min(a[i], left_min[i - 1])

    for i in range(n - 2, -1, -1):
        right_min[i] = min(a[i], right_min[i + 1])

    for i in range(1, n - 1):
        if a[i] > left_min[i - 1] and a[i] > right_min[i + 1]:
            continue
        else:
            answer += 1

    return answer


'''
1. 2개를 비교 시 번호가 작은 것을 삭제하는 방법은 1번 가능하다.
2. 가장 왼쪽과 가장 오른쪽은 항상 가능하다.
3. 중간에 존재하는 수는 왼쪽과 오른쪽을 따로 해준뒤 마지막에 3개의 수를 비교한다.
4. 만약 좌우 존재하는 수 2개가 자신보다 작을 경우 남아있지 못한다.
5. 그럼 자신을 기준으로 왼쪽과 오른쪽에서 가장 작은 수를 뽑으면 된다.
6. 그럼 O(n**2)인데 시간 초과가 발생한다.
7. 그럼 슬라이딩을 하여 왼쪽에 최소값과 left_min,right_min을 갱신해준다 -> 계속 사용을 x
8. 어쨋든 오른쪽 부분을 변경하는 과정에서 min 함수를 또 사용한다.
9. 왼쪽, 오른쪽 최소값 배열을 만들자.


'''