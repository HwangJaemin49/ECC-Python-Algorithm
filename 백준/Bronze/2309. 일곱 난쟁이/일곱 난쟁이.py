import sys

def input():
    return sys.stdin.readline().rstrip('\n')

total = []
s = 0

for _ in range(9):
    height = int(input())
    total.append(height)
s = sum(total) - 100

a = b = -1
for i in range(9):
    for j in range(i, 9):
        if total[i] + total[j] == s and i != j:
            a, b = i, j
            break
    if a != -1:
        break
total.pop(b)
total.pop(a)
total.sort()
for i in total:
    print(i)