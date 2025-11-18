def solution(scores):
    my_score = scores[0]
    my_sum = sum(my_score)

    scores = sorted(scores, key=lambda x: (-x[0], x[1]))

    max_b = 0
    valid = []

    for a, b in scores:
        if b < max_b:
            if [a, b] == my_score:
                return -1
        else:
            max_b = b
            valid.append(a + b)

    valid.sort(reverse=True)
    return valid.index(my_sum) + 1