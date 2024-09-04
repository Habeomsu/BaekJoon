import sys
a ,b = sys.stdin.readline().split()
a = a[::-1]
b = b[::-1]
if a > b:
    print(a)
else:
    print(b)