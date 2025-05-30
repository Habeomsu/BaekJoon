def solution(brown, yellow):
    answer = []
    for row in range(1, int(yellow ** 0.5) + 1):
        if yellow % row == 0:
            col = yellow / row
            if row * 2 + col * 2 + 4 == brown:
                break
    answer.append(col + 2)
    answer.append(row + 2)

    return answer