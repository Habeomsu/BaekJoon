def solution(gems):
    n = len(set(gems))
    gem_count = {}
    start, end = 0, 0
    gem_count[gems[0]] = 1
    answer = [1, len(gems)]

    while start < len(gems) and end < len(gems):

        if len(gem_count) == n:
            if (end - start) < (answer[1] - answer[0]):
                answer = [start + 1, end + 1]

            gem = gems[start]
            gem_count[gem] -= 1
            if gem_count[gem] == 0:
                del gem_count[gem]
            start += 1
        else:
            end += 1
            if end == len(gems):
                break
            gem = gems[end]
            if gem in gem_count:
                gem_count[gem] += 1
            else:
                gem_count[gem] = 1

    return answer
