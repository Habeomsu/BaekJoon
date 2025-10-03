def solution(alp, cop, problems):
    answer = 0

    INF = 10 ** 9
    alp_max = 0
    cop_max = 0

    for i in problems:
        alp_req, cop_req, alp_rwd, cop_rwd, cost = i
        alp_max = max(alp_max, alp_req)
        cop_max = max(cop_max, cop_req)

    dp = [[INF] * (cop_max + 1) for _ in range(alp_max + 1)]

    sa = min(alp, alp_max)
    sc = min(cop, cop_max)

    dp[sa][sc] = 0

    for a in range(sa, alp_max + 1):
        for c in range(sc, cop_max + 1):
            cur = dp[a][c]
            if cur == INF:
                continue

            if a + 1 <= alp_max:
                dp[a + 1][c] = min(dp[a + 1][c], cur + 1)
            if c + 1 <= cop_max:
                dp[a][c + 1] = min(dp[a][c + 1], cur + 1)

            for i in problems:
                alp_req, cop_req, alp_rwd, cop_rwd, cost = i

                if alp_req <= a and cop_req <= c:
                    na = min(alp_max, a + alp_rwd)
                    nc = min(cop_max, c + cop_rwd)
                    dp[na][nc] = min(dp[na][nc], cur + cost)

    answer = dp[alp_max][cop_max]

    return answer


'''

1. 최대 요구되는 알고력과, 코딩력을 구한다.
2. 주어진 알고력과, 코딩력을 최대 요구까지 올린다.
3. 알고력과 코딩력을 올리기 위한 방법은 1의 시간을 사용해서 각각 1을 올린다.
4. 문제를 해결이 가능하면 해결한 문제의 알고력과, 코딩력을 습득이 가능한다.

풀이 방법
1. 정렬은 두개중 큰수를 기준으로 정렬하고 같을 경우, 두 수의 합을 기준으로 정렬한다.
2. 정렬된 problems들을 반복해준다.
3. 만약 부족할 경우


아니면


조건
1. 만약 해당 문제를 풀수 있어서 문제를 풀었는데 cost보다 적게 증가하면 풀 필요가 없다. alp + cop < cost: -> 할필요가 없다.

2. 또한 1초당 증가량이 1보다 작아지면 굳이 문제를 풀 필요가 없어진다.

1. 



'''