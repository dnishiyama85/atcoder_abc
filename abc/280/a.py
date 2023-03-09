h, w = map(int, input().strip().split())
count = 0
for _ in range(h):
    row = list(input().strip())
    for c in row:
        if c == '#':
            count += 1

print(count)
