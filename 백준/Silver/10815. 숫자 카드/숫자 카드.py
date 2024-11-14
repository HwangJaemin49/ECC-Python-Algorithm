N = int(input())
listN = set(map(int, input().split()))
M = int(input())
listM = list(map(int, input().split()))
result = []

for num in listM:
    if num in listN:
        result.append(1)
    else:
        result.append(0)

for i in result:
    print(i, end = " ")