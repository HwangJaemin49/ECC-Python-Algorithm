from collections import deque

n, m = map(int, input().split())

r, c, d = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

visited = [[False] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
count = 0

def bfs(x, y, d):

    global count
    queue = deque()
    visited[x][y] = True
    count += 1
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        turn = 0
        for i in range(4):
            d = (d+3)%4
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    count += 1
                    queue.append((nx, ny))
                    turn = 1
                    break
        if turn == 0:
            bx = x - dx[d]
            by = y - dy[d]
            if graph[bx][by] == 1:
                print(count)
                break
            else:
                queue.append((bx, by))

bfs(r, c, d)