H , M = input().split()
H,M=int(H),int(M)
A = int(input())

M = M + A
if M >= 60:
    H = H + M //60
    M = M % 60
print(H%24,M)