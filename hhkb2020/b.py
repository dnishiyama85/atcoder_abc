h, w = map(int, input().strip().split())
ss = [input().strip() for _ in range(h)]

total = 0
for i in range(h):
    for j in range(w):
        current = ss[i][j]
        left = ss[i][j + 1] if j < w - 1 else '#'
        down = ss[i + 1][j] if i < h - 1 else '#'
        if current == '.' and left == '.':
            total += 1
        if current == '.' and down == '.':
            total += 1

print(total)
