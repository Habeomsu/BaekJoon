from collections import deque
def solution(n, computers):
    answer = 0
    node = [[] for _ in range(n)]
    for i in range(n):
        com = computers[i]
        for j in range(n):
            if j == i:
                continue
            else:
                if com[j] == 1:
                    node[i].append(j)
    visited = [False] * n

    def bfs(start):
        que = deque([start])
        que.append(start)
        visited[start] = True
        while que:
            now = que.popleft()
            for i in node[now]:
                if visited[i] == False:
                    que.append(i)
                    visited[i] = True
    for i in range(n):
        if visited[i] == False:
            bfs(i)
            answer +=1

    return answer



'''

방문 처리를 통해서 bfs 를 실행한다.
전체 숫자 만큼 for문을 돌려서 만약에 해당 방문 값이 false 이면 answer +1 해준다.



'''