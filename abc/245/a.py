a, b, c, d = map(int, input().strip().split())

takahashi = a * 60 * 60 + b * 60
aoki = c * 60 * 60 + d * 60 + 1

if takahashi <= aoki:
    print('Takahashi')
else:
    print('Aoki')
