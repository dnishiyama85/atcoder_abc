a, b = map(int, input().strip().split())

if 0 < a:
    print('Positive')
elif 0 <= b:
    print('Zero')
else:
    if (b - a) % 2 == 0:
        print('Negative')
    else:
        print('Positive')
