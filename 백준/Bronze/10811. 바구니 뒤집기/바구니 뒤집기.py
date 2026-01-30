import sys

def input():
    return sys.stdin.readline().rstrip('\n')

N, M = map(int, input().split())
baskets = [i for i in range(0, N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    baskets[a:b+1] = baskets[a:b+1][::-1]
baskets.remove(0)

for basket in baskets:
    print(basket, end=' ')