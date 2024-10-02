from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

array = list(map(int, input().split()))  # 빼내야 하는 위치

queue = deque(range(1, n+1))  # 수가 담겨 있는 큐

move = 0  # 움직인 횟수

for i in array:
    while True:
        if queue[0] == i:
            queue.popleft()
            break
        else:
            if queue.index(i) <len(queue)/2:
                while queue[0] != i:
                    queue.rotate(-1)
                    move += 1
            else:
                while queue[0] != i:
                    queue.rotate(+1)
                    move += 1
print(move)