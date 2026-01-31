import sys

def input():
    return sys.stdin.readline().rstrip('\n')

chess = []
cnt = 0
total = 0

for i in range(8):
    chess.append(input())

for row in chess:
    if cnt % 2 == 0:
        for i in range(0, 8, 2):
            if row[i] == 'F':
                total += 1
    else:
        for i in range(1, 8, 2):
            if row[i] == 'F':
                total += 1
    cnt += 1
print(total)