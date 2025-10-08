def solution(n, m, x, y, r, c, k):
    answer = ''

    xy_sum = abs(r - x) + abs(c - y)
    if xy_sum > k or (xy_sum + k) % 2 == 1:
        return 'impossible'

    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]

    sdl_sum = abs(x - n) + abs(y - 1)
    edl_sum = abs(r - n) + abs(c - 1)

    if sdl_sum + edl_sum <= k:
        start_str = ''
        end_str = ''
        middle_str = ''
        for _ in range(abs(x - n)):
            start_str += 'd'
        for _ in range(abs(y - 1)):
            start_str += 'l'
        for _ in range(abs(c - 1)):
            end_str += 'r'
        for _ in range(abs(r - n)):
            end_str += 'u'
        for _ in range((k - (sdl_sum + edl_sum)) // 2):
            middle_str += 'rl'
        answer = answer + start_str + middle_str + end_str

    else:
        cx, cy = x, y
        for step in range(k):
            for i, ch in enumerate('dlru'):
                nx = cx + dx[i]
                ny = cy + dy[i]
                if not (1 <= nx <= n and 1 <= ny <= m):
                    continue
                rem = k - (step + 1)
                dist = abs(r - nx) + abs(c - ny)
                if rem >= dist:
                    answer += ch
                    cx = nx
                    cy = ny
                    break

    return answer


'''
dd




1. 완전 탐색은 불가능하다. -> 4**2500이다
2. d,l,r,u 순이 사전순이다. 아래, 왼쪽, 오른쪽, 위 
3. 불가능한 경우는 두 좌표의 차가 홀수 인 경우 -> k가 짝수, 홀수인 경우 -> k가 홀수인경우 이다.
4. d -> 최대한 빨리, u -> 최대한 나중에 -> 
5. 현재 위치를 계속 기록해둔다, 목표와 현재 위치의 거리를 구한다.-> 만약 k일 경우 최단 거리를 구해야한다. -> 


1. s,e 의 좌표의 차의 합을 구한다. -> xy_sum
2. 만약 xy_sum < k or (xy_sum + k)% 2 != 0 -> impossible
3. k의 범위 따라 구하는 값이 달라진다.
    3.1 s와 가장 왼쪽의 위치 좌표의 차의 합을 구한다. -> sdl_sum
    3.2 e와 가장 왼쪽의 위치 좌표의 차의 합을 구한다. -> edl_sum
    3.3 만약 sdl_sum + edl_sum 보다 k가 클 경우 -> 차 만큼 사이의 lr을 반복해준다.
    3.4 만약 sdl_sum + edl_sum > k 일 경우 -> 


'''