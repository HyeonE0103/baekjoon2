import sys

n, x = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
small_number = []


for i in range(n):
    if numbers[i] < x:
        sys.stdout.write(str(numbers[i])+" ")
