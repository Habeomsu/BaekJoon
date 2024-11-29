import sys

string = sys.stdin.readline()
result=''
result = string.replace('XXXX','AAAA')
result = result.replace('XX','BB')
if(result.count('X')>=1):
    print(-1)
else:
    print(result)