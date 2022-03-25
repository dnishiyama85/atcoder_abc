a, b, c, x = map(int, input().strip().split())

if x <= a:
    print(1.0)
elif x <= b:
    print(c / (b - a))
else:
    print(0.0)
