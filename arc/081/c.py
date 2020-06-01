from collections import defaultdict

n = int(input())
as_ = map(int, input().strip().split())

d = defaultdict(int)

for a in as_:
    d[a] += 1

rects = sorted([k for k, v in d.items() if v >= 2], reverse=True)
squares = sorted([k for k, v in d.items() if v >= 4], reverse=True)

max_rect = rects[0] * rects[1] if len(rects) >= 2 else 0
max_square = squares[0] ** 2 if len(squares) > 0 else 0

print(max(max_rect, max_square))
