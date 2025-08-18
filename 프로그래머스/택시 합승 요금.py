import heapq


def solution(n, s, a, b, fares):
    answer = int(1e9)
    node = [[] for _ in range(n + 1)]
    for i in fares:
        c, d, e = i
        node[c].append((d, e))
        node[d].append((c, e))

    dist1 = dijkstra(n, s, node)
    answer = dist1[a - 1] + dist1[b - 1]
    for i in range(1, n + 1):
        if i == s:
            continue
        dist2 = dijkstra(n, i, node)
        taxi_cost = dist1[i - 1] + dist2[a - 1] + dist2[b - 1]
        answer = min(answer, taxi_cost)
    return answer


def dijkstra(n, start, graph):
    INF = int(1e9)
    dist = [INF] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        cost, now = heapq.heappop(q)
        if dist[now] < cost:
            continue
        for i in graph[now]:
            next_node, next_cost = i
            if dist[next_node] >= next_cost + cost:
                dist[next_node] = next_cost + cost
                heapq.heappush(q, (next_cost + cost, next_node))
    return dist[1:]


'''

1. 다익스트라 함수를 만든다. -> dijkstra()
2. 시작지점에서 다익스트라함수를 사용한다. -> 처음 다익스트라값 dist1
3. answer 에값은 dist1[a-1] + dist1[b-1] 을 초기값으로 설정한다.
4. 시작지점을 제외한 모든 방향에서 다익스트라 사용후 a,b 에 값을 구한다. -> 두번째 다익스트라값 dist2
5. dist1[i-1] + dist2[a-1] + dist2[b-1] 한값이 최소인 경우를 구한다. -> min() 함수 사용



'''