import sys
def input():
    return sys.stdin.readline().rstrip('\n')

T = int(input())

coins = [25, 10, 5, 1]

for _ in range(T):
    cost = int(input())
    ans = []
    for coin in coins:
        q, cost = divmod(cost, coin)
        ans.append(q)
    print(*ans)