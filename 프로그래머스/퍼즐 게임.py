def solution(diffs, times, limit):
    answer = 0
    Max = max(diffs)
    Min = 1
    while Min <= Max:
        mid = (Max + Min) // 2
        total_time = 0
        for i in range(len(diffs)):
            if mid >= diffs[i]:
                total_time += times[i]
            else:
                if i == 0:
                    total_time = total_time + (diffs[i] - mid) * times[i]
                else:
                    total_time = total_time + (diffs[i] - mid) * (times[i] + times[i - 1]) + times[i]
        if total_time <= limit:
            Max = mid - 1
        else:
            Min = mid + 1

    return Max + 1

### 난이도를 구하라 x
### diffs 에서 가장 큰수를 최대값으로 잡고 줄여나간다
### 만약 문제를 실패하면 diff + 1값이 답이다
### 소요 시간은 (diff - level)*(times)+time_cur 이다
### 처음부터 큰수 부터 작은수로 가면 시간 초과가 뜬다
### 이분 탐색으로 구한다.
