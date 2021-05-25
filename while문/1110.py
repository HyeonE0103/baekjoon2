import sys

num = int(sys.stdin.readline())
num2 = num
count = 0
while True:
    a = num // 10
    b = num % 10
    sum = a +b
    num = (b * 10) + (sum % 10)
    count = count + 1
    if num == num2:
        break

sys.stdout.write(str(count))
