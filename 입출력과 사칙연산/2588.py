a = int(input())
b = int(input())
d=b

for i in range(3):
    c = int(d%10)
    print(a*c)
    d = int(d/10)

print(a*b)