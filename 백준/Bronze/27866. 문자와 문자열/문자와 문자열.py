import sys
def input():
    return sys.stdin.readline().rstrip('\n')

alphs = list(input())
i = int(input())
print(alphs[i-1])