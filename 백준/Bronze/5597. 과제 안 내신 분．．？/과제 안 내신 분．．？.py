import sys

def input():
    return sys.stdin.readline().rstrip('\n')

students = [i for i in range(1, 31)]
submits = []

for i in range(1, 29):
    submit = int(input())
    students.remove(submit)

for student in students:
    print(student)