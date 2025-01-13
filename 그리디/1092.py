import sys


n = int(sys.stdin.readline())
cweight = list(map(int,sys.stdin.readline().split()))

m = int(sys.stdin.readline())
bweight = list(map(int,sys.stdin.readline().split()))

cweight = sorted(cweight,reverse=True)
bweight = sorted(bweight,reverse=True)

result =0

if bweight[0]>cweight[0]:  # 가장 무거운 것을 들 수 있는 크레인이 박스 무게 보다 작으면 -1
    result = -1
else:
    while bweight:
        for c in cweight:
            if bweight and c<bweight[-1]:
                continue
            for b in bweight:
                if c >=b:
                    bweight.remove(b)
                    break
        result+=1

print(result)
