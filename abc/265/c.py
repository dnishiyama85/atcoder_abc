h, w = map(int, input().strip().split())

visited = [[False] * w for _ in range(h)]
cells = []
for _ in range(h):
    row = list(input().strip())
    cells.append(row)

y, x = 0, 0
visited[y][x] = True

while True:
    command = cells[y][x]
    loop = False
    if command == 'U':
        if y > 0:
            y -= 1
        else:
            break
    elif command == 'D':
        if y < h - 1:
            y += 1
        else:
            break
    elif command == 'L':
        if x > 0:
            x -= 1
        else:
            break
    elif command == 'R':
        if x < w - 1:
            x += 1
        else:
            break
    else:
        break

    if visited[y][x]:
        loop = True
        break
    else:
        visited[y][x] = True


if loop:
    print(-1)
else:
    print(f'{y + 1} {x + 1}')
