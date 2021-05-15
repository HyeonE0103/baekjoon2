import sys

try:
    while True:
        a,b = map(int, sys.stdin.readline().split())
        sys.stdout.write(str(a+b) + '\n')

except:
    print("")

"""
try 안에 있는 소스에서 오류가 나면 파이썬 터미널 창에
바로 에러를 표시하지 않고 except 안에 있는 구문을 실행시킴
"""