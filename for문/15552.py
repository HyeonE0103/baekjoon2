import sys

answer = []

n = int(sys.stdin.readline())

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    c = a+b
    answer.append(c)

for i in range(n):
    sys.stdout.write(str(answer[i]) + '\n')