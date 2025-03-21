### 우선순위가 존재하는 것들은 묶어버린다 ...
###  heapq 를 생성하는데 만약에 묶인 수중 앞에가 더 클경우 그냥

import sys

n = int(sys.stdin.readline())
dict ={}
node, start,end =sys.stdin.readline().split()
dict[node]=start,end
for i in range(1,n):
    a,b,c = sys.stdin.readline().split()
    dict[a]=b,c



def preorder(node):
    if node != '.':
        print(node,end="")
        preorder(dict[node][0])
        preorder(dict[node][1])

def inorder(node):
    if node != '.':
        inorder(dict[node][0])
        print(node,end="")
        inorder(dict[node][1])

def postorder(node):
    if node != '.':
        postorder(dict[node][0])
        postorder(dict[node][1])
        print(node,end="")

preorder('A')
print("")
inorder('A')
print("")
postorder('A')
