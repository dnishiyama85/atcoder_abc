x, y = map(int, input().strip().split())

# 鶴: c, 亀: t
#   c +   t = x
# 2 c + 4 t = y

found = False
for c in range(101):
    for t in range(101):
        if c + t == x and 2 * c + 4 * t == y:
            found = True

if found:
    print('Yes')
else:
    print('No')
