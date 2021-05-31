n = []
for i in range(9) :
    n.append(int(input()))

big = n[0]

for i in n :
    if i >big :
        big = i

print(big)
print(n.index(big) + 1)
