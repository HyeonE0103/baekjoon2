import sys

n = int(sys.stdin.readline())

for i in range(n, 0, -1):
    for j in range(1, n+1, 1):
        if j >= i:
            sys.stdout.write("*")
        else:
            sys.stdout.write(" ")
    sys.stdout.write('\n')