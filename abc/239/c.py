x1, y1, x2, y2 = map(int, input().strip().split())

set1 = set([
    (x1 + 1, y1 + 2), (x1 + 2, y1 + 1), (x1 + 2, y1 - 1), (x1 + 1, y1 - 2),
    (x1 - 1, y1 + 2), (x1 - 2, y1 + 1), (x1 - 2, y1 - 1), (x1 - 1, y1 - 2),
])

set2 = set([
    (x2 + 1, y2 + 2), (x2 + 2, y2 + 1), (x2 + 2, y2 - 1), (x2 + 1, y2 - 2),
    (x2 - 1, y2 + 2), (x2 - 2, y2 + 1), (x2 - 2, y2 - 1), (x2 - 1, y2 - 2),
])

if len(set1 & set2) > 0:
    print('Yes')
else:
    print('No')
