def solution(s):
    answer = 1

    n = len(s)

    for i in range(1, n - 1):
        mid = i
        count = 1
        left = i - 1
        right = i + 1
        while left >= 0 and right < n:
            if s[left] == s[right]:
                count += 2
                left -= 1
                right += 1
            else:
                break
        if answer <= count:
            answer = count

    for i in range(0, n - 1):
        left = i
        right = i + 1
        count = 0
        while left >= 0 and right < n:
            if s[left] == s[right]:
                count += 2
                left -= 1
                right += 1
            else:
                break
        if answer <= count:
            answer = count

    return answer