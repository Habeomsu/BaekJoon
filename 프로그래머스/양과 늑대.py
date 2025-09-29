def solution(info, edges):
    answer = 0
    node = [[] for _ in range(len(info))]
    for i in edges:
        a, b = i
        node[a].append(b)

    max_sheep = 0

    def back(arr, avail_arr, sheep_num, wolf_num):
        nonlocal max_sheep
        if len(arr) == len(info):
            if max_sheep < sheep_num:
                max_sheep = sheep_num
            return

        if sheep_num > max_sheep:
            max_sheep = sheep_num

        for i in avail_arr:
            if i in arr:
                continue
            temp_sheep = sheep_num
            temp_wolf = wolf_num
            if info[i] == 0:
                temp_sheep += 1
            else:
                temp_wolf += 1
            if temp_sheep <= temp_wolf:
                continue

            new_avail = set(avail_arr)
            new_avail.remove(i)
            new_avail = list(new_avail)
            for j in node[i]:
                if j not in arr:
                    new_avail.append(j)
            arr.append(i)
            back(arr, new_avail, temp_sheep, temp_wolf)
            arr.pop()

    back([], [0], 0, 0)

    answer = max_sheep
    return answer


'''

시도 방법
1. dfs, bfs 둘다 아니다.
    -> dfs가 아닌 이유 0번 -> 1번 -> 8번 이렇게 가는게 존재한다.
    -> bfs가 아닌 이유 0번 -> 1번 -> 8번 -> 9번 -> 4번 -> 6번 이 존재한다.
    -> 즉 늑대의 수와 양의 수를 비교하고 다음에 늑대 인지 양인지도 중요하다.
2. 뒤에서 부터 올라가기??
3. 완전 탐색으로 모든 경우의 수를 찾기? -> info가 2부터 17까지라 17펙토리얼 
    3.1 근데 완전히 펙토리얼은 아니다. 해당 노드에서 갈수 있는 경우와 이전 노드들의 분기 점을 갈 수가 있다.
    3.2 완전 탐색을 진행하는데, 갈 수 있는 모든 노드들의 배열을 따로 만들어둔다.
    3.3 그래서 해당 배열을 순회한다.
    3.4 단, 순회와 동시에 갈수 있는 배열의 자신의 자식 노드들을 추가한다.
4. 문제는 왔던 곳을 지나가서 이전으로 가는게 가능한 것이다. 
5. 또한 늑대를 먹어도 다음에 양을 먹을 수 있는 경우가 존재하면 가능한것이다.


문제 풀이
1. 늑대의 수 >= 양 -> 양이 다 죽는다. 즉, 늑대의 수 < 양
2. 노드당 포함하는 자식노드 배열을 만든다.
3. dfs 를 통한 백트래킹을 한다.
4. 이동 가능한 배열들과 현재 이동된 배열들을 통해 벡트래킹을 완성한다. 
5. 시간초과가 난다.


'''