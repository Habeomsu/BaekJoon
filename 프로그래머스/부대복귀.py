import heapq


def solution(n, roads, sources, destination):
    answer = []

    node = [[] for _ in range(n + 1)]

    for road in roads:
        a, b = road
        node[a].append(b)
        node[b].append(a)

    INF = int(1e9)

    visited = [INF] * (n + 1)

    def dijkstra(start, visited):
        que = []
        heapq.heapify(que)
        heapq.heappush(que, [0, start])
        visited[start] = 0
        while que:
            cost, now_node = heapq.heappop(que)

            if cost > visited[now_node]:
                continue

            for next_node in node[now_node]:
                next_cost = 1
                if visited[next_node] >= next_cost + cost:
                    visited[next_node] = next_cost + cost
                    heapq.heappush(que, [visited[next_node], next_node])

    dijkstra(destination, visited)

    for source in sources:
        if visited[source] == INF:
            answer.append(-1)
        else:
            answer.append(visited[source])

    return answer


'''

1. destination에서 모든 sources 까지 최단 경로를 구하면 된다.
2. 다익스트라를 사용하면 된다.


'''