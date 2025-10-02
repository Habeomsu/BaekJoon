import heapq


def solution(n, paths, gates, summits):
    answer = []
    nodes = [[] for _ in range(n + 1)]

    ## 노드 만들기
    for i in paths:
        a, b, c = i
        nodes[a].append([b, c])
        nodes[b].append([a, c])

    INF = int(1e9)
    intensitys = [INF] * (n + 1)

    gates_set = set(gates)
    summits_set = set(summits)

    hq = []
    heapq.heapify(hq)
    for i in gates:
        intensitys[i] = 0
        heapq.heappush(hq, [0, i])

    while hq:
        cost, node = heapq.heappop(hq)

        if intensitys[node] < cost:
            continue

        if node in summits_set:
            continue

        for i in nodes[node]:
            next_node, next_cost = i
            if next_node in gates_set:
                continue

            new_its = max(next_cost, cost)

            if intensitys[next_node] > new_its:
                intensitys[next_node] = new_its
                heapq.heappush(hq, [new_its, next_node])

    min_intensity = INF
    avail = []

    for i in summits:
        intensity = intensitys[i]
        if min_intensity >= intensity:
            avail.append([i, intensity])

    avail = sorted(avail, key=lambda x: (x[1], x[0]))

    return avail[0]


'''

1. 과연 다익스트라를 사용하는게 맞을까??
2. 차라리 dfs를 사용하는게 맞을까?? 

생각해보면 -> 왔던길을 그대로 다시가면 된다.
애초에 처음갈때 최선의 길을 간다면, 다시 안와도 된다.
즉 -> 모든 가능한 경우를 계속 구해보자 (dfs , 벡트래킹 )
그러면 가면서 계속 intensity를 변경하거나 구해준다.
만약 이미 구한 intensity보다 크면 그것은 더이상 구할 필요가 없다.



1. 다익스트라를 기반으로 문제를 해결한다.
2. 출입구의 수만큼 비교를 해야한다.
3. 산봉우리들이 여러개 일 수가 있다. -> 다익스트라를 for 문을 통해 n번 반복한다.
4. 노드 사이의 관계를 표현하는 배열을 만든다 -> node 
5. 다익스트라 함수를 만든다.
    5.1 출입구에서 산봉우리로 가는 최단 거리를 만들어야한다.
    5.2 움직일때 마다 intensity를 갱신해야한다.
    5.3 해당 노드에서 여러 노드를 방문이 가능 할 경우
        5.3.1 다음 노드는 출입구면 안된다. -> 출입구일경우 pass
        5.3.2 다음 노드들이 여러개일 경우 -> 사이의 거리가 intensity보다 작야아한다.
            5.3.2.1 만약, intensity보다 작은 노드들이 여러개일 경우 -> 노드가 작은 곳으로 이동한다.
        5.3.3 다음 노드들이 하나일 경우 -> 어쩔 수 없이 이동해야한다. 단, 거리가 intensity보다 클 경우 intensity를              변경해준다.




'''


'''

1. 과연 다익스트라를 사용하는게 맞을까??
2. 차라리 dfs를 사용하는게 맞을까?? 

생각해보면 -> 왔던길을 그대로 다시가면 된다.
애초에 처음갈때 최선의 길을 간다면, 다시 안와도 된다.
즉 -> 모든 가능한 경우를 계속 구해보자 (dfs , 벡트래킹 )
그러면 가면서 계속 intensity를 변경하거나 구해준다.
만약 이미 구한 intensity보다 크면 그것은 더이상 구할 필요가 없다.



1. 다익스트라를 기반으로 문제를 해결한다.
2. 출입구의 수만큼 비교를 해야한다.
3. 산봉우리들이 여러개 일 수가 있다. -> 다익스트라를 for 문을 통해 n번 반복한다.
4. 노드 사이의 관계를 표현하는 배열을 만든다 -> node 
5. 다익스트라 함수를 만든다.
    5.1 출입구에서 산봉우리로 가는 최단 거리를 만들어야한다.
    5.2 움직일때 마다 intensity를 갱신해야한다.
    5.3 해당 노드에서 여러 노드를 방문이 가능 할 경우
        5.3.1 다음 노드는 출입구면 안된다. -> 출입구일경우 pass
        5.3.2 다음 노드들이 여러개일 경우 -> 사이의 거리가 intensity보다 작야아한다.
            5.3.2.1 만약, intensity보다 작은 노드들이 여러개일 경우 -> 노드가 작은 곳으로 이동한다.
        5.3.3 다음 노드들이 하나일 경우 -> 어쩔 수 없이 이동해야한다. 단, 거리가 intensity보다 클 경우 intensity를              변경해준다.




'''