import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n, m = map(int, input().split())
    k = int(input())

    maps = [[0] * (m + 2) for _ in range(n + 2)]
    maps[1][1] = 1

    end = set()
    load = set()

    for _ in range(k):
        a, b, c, d = map(int, input().split())
        (a, b), (c, d) = sorted([(a + 1, b + 1), (c + 1, d + 1)])
        end.add((c, d))
        load.add((a, b, c, d))

    for y in range(1, n + 2):
        for x in range(1, m + 2):
            if y == 1 and x == 1: continue

            if (y, x) in end:
                if (y - 1, x, y, x) not in load:
                    maps[y][x] = maps[y - 1][x]
                elif (y, x - 1, y, x) not in load:
                    maps[y][x] = maps[y][x - 1]
            else:
                maps[y][x] = maps[y - 1][x] + maps[y][x - 1]

    print(maps[n + 1][m + 1])