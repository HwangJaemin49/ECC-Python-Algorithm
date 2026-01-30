import sys
def input():
    return sys.stdin.readline().rstrip('\n')

N = int(input())
l = N //4

print('long ' * l + 'int')