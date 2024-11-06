N = int(input())
nums = []
for i in range(N):
    num = int(input())

lists.sort(key = lambda x : (x[1], x[0]))

for list in lists:
  print(list[0], list[1])
