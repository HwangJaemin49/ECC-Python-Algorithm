import sys

def input():
    return sys.stdin.readline().rstrip('\n')

board = [[0]*101 for _ in range(101)]
total = 0

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            if board[i][j] == 0:
                board[i][j] = 1
            else:
                continue

for row in board:
    for r in row:
        if r == 1:
            total += 1

print(total)
