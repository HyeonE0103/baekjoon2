import sys


n = int(sys.stdin.readline())

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    sys.stdout.write("Case #"+str(i+1)+": "+str(a)+" + "+str(b)+" = "+str(a+b)+'\n')
