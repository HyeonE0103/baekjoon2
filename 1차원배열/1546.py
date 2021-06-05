n = int(input())
numbers = list(map(int, input().split()))

max_num = max(numbers)
sum = 0

for i in numbers:
    num = i/max_num*100
    sum = sum + num

print(sum/n)