import sys

def input():
    return sys.stdin.readline().rstrip('\n')

nums = []
max = -1
x, y = 0, 0

for row in range(9):
    row = list(map(int, input().split()))
    nums.append(row)
for i in range(9):
    for j in range(9):
        if nums[i][j] > max:
            max = nums[i][j]
            x = i
            y = j
print(max, x+1, y+1)