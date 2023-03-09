n = int(input())
black = []
for _ in range(n):
    x, y = map(int, input().strip().split())
    black.append((x, y))

black = set(black)

connected = 0
visited = set()

for b in black:
    if b in visited:
        continue

    connected += 1

    stack = [b]
    visited.add(b)

    while len(stack) > 0:
        cell = stack.pop()
        i, j = cell
        adjacents = [
                (i, j + 1), (i + 1, j + 1),
            (i - 1, j),              (i + 1, j),
                (i - 1, j - 1), (i, j - 1),
        ]
        for adj in adjacents:
            if adj in visited:
                continue
            visited.add(adj)
            if adj in black:
                stack.append(adj)

print(connected)
