import sys

def input():
    return sys.stdin.readline().rstrip('\n')


N, M = map(int, input().split())

basket = [i for i in range(1, N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    if a == b:
        continue
    basket[a-1], basket[b-1] = basket[b-1], basket[a-1]

for num in basket:
    print(num, end=' ')