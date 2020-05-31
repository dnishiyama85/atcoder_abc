R, G, B, N = map(int, input().strip().split())

count = 0
for r in range(3001):
    for g in range(3001):
        rest = N - r * R - g * G
        if rest >= 0 and rest % B == 0:
            count += 1

print(count)
