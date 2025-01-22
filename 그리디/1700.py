import sys

n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

now_arr = []  # 현재 멀티탭에 꽂혀 있는 플러그들
total = 0  # 플러그를 뺀 횟수

for i in range(k):
    a = arr[i]

    # 현재 멀티탭에 꽂혀 있는 플러그가 모두 꽉 차 있지 않은 경우
    if a not in now_arr:
        if len(now_arr) < n:
            now_arr.append(a)  # 꽂지 않은 플러그라면 추가
        else:
            # 현재 멀티탭이 꽉 찼다면, 다음 사용이 가장 늦은 것을 찾아서 교체
            # 다음 사용 정보를 저장
            next_use = {}
            for j in range(i + 1, k):
                if arr[j] in now_arr and arr[j] not in next_use:
                    next_use[arr[j]] = j

            # 현재 멀티탭에 꽂혀 있는 플러그 중에서 다음 사용이 가장 늦은 것을 찾기
            last_use_index = -1
            plug_to_remove = -1
            for plug in now_arr:
                if plug not in next_use:
                    plug_to_remove = plug
                    break
                if next_use[plug] > last_use_index:
                    last_use_index = next_use[plug]
                    plug_to_remove = plug

            # 멀티탭에서 플러그를 제거하고 새로운 플러그를 꽂기
            now_arr.remove(plug_to_remove)
            now_arr.append(a)
            total += 1  # 플러그를 뺀 횟수 증가

print(total)
