import sys

def input():
    return sys.stdin.readline().rstrip('\n')

N = int(input())
spots = [[0]*100 for _ in range(100)]

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            spots[i][j] = 1
ans = sum(sum(row) for row in spots)
print(ans)
