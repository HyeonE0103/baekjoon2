import sys

n = int(sys.stdin.readline())
a = 0
for i in range(n):
    a = a + (i+1)

sys.stdout.write(str(a))