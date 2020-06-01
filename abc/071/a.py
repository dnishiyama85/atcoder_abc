x, a, b = map(int, input().strip().split())
if abs(x - a) < abs(x - b):
    print('A')
else:
    print('B')
