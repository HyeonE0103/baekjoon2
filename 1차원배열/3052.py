numbers = [int(input()) % 42 for i in range(10)]
num = 0

for j in range(0,43):
    if numbers.count(j) != 0:
        num = num + 1

print(num)
