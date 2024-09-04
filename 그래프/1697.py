import sys
from collections import deque

def bfs(start, target):
    q = deque([start])
    distances = [-1] * 100001
    distances[start] = 0
    while q:
        current = q.popleft()
        if current == target:
            return distances[current]
        for next_pos in (current - 1, current + 1, current * 2):
            if 0 <= next_pos <= 100000 and distances[next_pos] == -1:
                distances[next_pos] = distances[current] + 1
                q.append(next_pos)

N, K = map(int, sys.stdin.readline().split())
result = bfs(N, K)
print(result)