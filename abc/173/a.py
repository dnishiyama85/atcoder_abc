n = int(input())
n %= 1000
if n == 0:
    print(0)
else:
    print(1000 - n)
