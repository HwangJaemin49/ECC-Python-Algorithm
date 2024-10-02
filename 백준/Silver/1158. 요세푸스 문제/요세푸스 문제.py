from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

result = []

move = 0
queue = deque(range(1, n+1))

while (len(queue) > 0) :
    if move != k-1 :
        queue.rotate(-1)
        move += 1
    else :
        result.append(queue.popleft())
        move = 0

print("<", end="")
for i in range(len(result)-1):
  print(result[i], end=", ")
print(str(result[len(result)-1])+">")