tree = {}

n = int(input())

for _ in range(n):
    root, left, right = input().split()
    tree[root] = [left, right]

def preorder(node): # 전위 순회
    if node != '.':
        print(node, end='')
        preorder(tree[node][0]) # 왼쪽 자식 순회
        preorder(tree[node][1]) # 오른쪽 자식 순회

def inorder(node): # 중위 순회
    if node != '.':
        inorder(tree[node][0])
        print(node, end='')
        inorder(tree[node][1])

def postorder(node):
    if node != '.':
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')