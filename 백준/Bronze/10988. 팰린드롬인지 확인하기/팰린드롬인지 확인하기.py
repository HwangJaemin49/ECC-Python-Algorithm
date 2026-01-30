import sys

def input():
    return sys.stdin.readline().rstrip('\n')

word = list(input())
reverse = word[::-1]

cnt = 0

for i in range(len(word)):
    if word[i] == reverse[i]:
        cnt+=1
if cnt == len(word):
    print(1)
else:
    print(0)
