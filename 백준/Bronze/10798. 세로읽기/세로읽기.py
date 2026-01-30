import sys

def input():
    return sys.stdin.readline().rstrip('\n')

word = []
new = []

for _ in range(5):
    word.append(list(input()))

for c in range(15):
    for r in range(5):
        if c < len(word[r]):
            new.append(word[r][c])
print(''.join(new))
