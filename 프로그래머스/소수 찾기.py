def solution(numbers):
    answer = 0
    number_list = list(numbers)
    number_set = set()

    def back(arr, length):
        result = []

        def permute(path, used):
            if len(path) == length:
                result.append(path[:])
                return
            for i in range(len(arr)):
                if not used[i]:
                    used[i] = True
                    path.append(arr[i])
                    permute(path, used)
                    path.pop()
                    used[i] = False

        permute([], [False] * len(arr))
        return result

    for i in range(1, len(number_list) + 1):
        result = back(number_list, i)
        for i in result:
            num = int(''.join(i))
            number_set.add(num)

    set_list = list(number_set)
    for i in set_list:
        if i >= 2:
            a = True
            for j in range(2, i):
                if i % j == 0:
                    a = False
                    break
            if a == True:
                answer += 1

    return answer
