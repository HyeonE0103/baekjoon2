total = 1
for i in range(3):
    num = int(input())
    total = total * num

total_str = str(total)

for i in range(10):
    num_count = total_str.count(str(i))
    print(num_count)

