import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
tree = {}

for _ in range(n-1) :
    parent, child, weight = map(int, input().split())

    if parent not in tree:
        tree[parent] = []
    if child not in tree:
        tree[child] = []
    tree[parent].append((child, weight))
    tree[child].append((parent, weight)) # 양방향 트리이므로 양쪽 다 추가

def dfs(node, distance):
    visited[node] = True
    farthest_node = node
    max_distance = distance
    for neighbor, dist in tree.get(node, []):
        if not visited[neighbor]:
            new_distance, new_node = dfs(neighbor, distance + dist)
            if new_distance > max_distance:
                max_distance = new_distance
                farthest_node = new_node
    return max_distance, farthest_node

visited = [False]*(n+1)
_, farthest_node = dfs(1, 0)

visited = [False]*(n+1)
diameter, _ = dfs(farthest_node, 0)

print(diameter)