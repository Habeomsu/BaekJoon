def solution(n, works):
    answer = 0
    works_sum = sum(works)

    if works_sum <= n:
        return 0

    works = sorted(works)

    start = 0
    end = works[-1]
    default = 0
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for work in works:
            if work >= mid:
                total = total + work - mid
        if total >= n:
            start = mid + 1
        else:
            end = mid - 1

    default = start

    left_n = n

    works = sorted(works, reverse=True)

    for i in range(len(works)):
        if left_n == 0:
            break

        if works[i] > default:
            if left_n >= works[i] - default:
                left_n = left_n - works[i] + default
                works[i] = default
            else:
                works[i] = works[i] - left_n
                left_n = 0
    i = 0

    while left_n > 0:
        works[i] = works[i] - 1
        i += 1
        i = i % len(works)
        left_n -= 1

    for work in works:
        answer += work * work

    return answer


'''

야근 지수를 줄이기 위해서는 남은 잔업량들의 제곱이 작아야한다.
1. works 의 sum을 구해준다. -> 만약 n 보다 작다면 답은 0이다.
2. works 배열을 역순으로 정렬해준다.
3. 0 과 최대값을 구한다.
4. mid 값을 기준으로 빼면서 n의 수를 만족하는 구해준다.
즉, 이분 탐색을 이용해서 



'''