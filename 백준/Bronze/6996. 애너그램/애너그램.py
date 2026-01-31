import sys

def input():
    return sys.stdin.readline().rstrip('\n')

T = int(input())

for _ in range(T):
    A, B = map(str, input().split())
    Alist = list(A)
    Blist = list(B)
    if (sorted(Alist) == sorted(Blist)):
        print(A + ' & ' + B + ' are anagrams.')
    else:
        print(A + ' & ' + B + ' are NOT anagrams.')
