N = int(input())
lists = []
for i in range(N):
    age, name = map(str, input().split())
    lists.append((age, name))

lists.sort(key = lambda x : x[0])

for list in lists:
  print(list[0], list[1])
