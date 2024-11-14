N = int(input())
listN = set(map(int, input().split()))
M = int(input())
listM = list(map(int, input().split()))

for M in listM:
    if M in listN:
        print(1)
    else:
        print(0)
