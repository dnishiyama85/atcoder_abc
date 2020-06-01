x1, y1, x2, y2 = map(int, input().strip().split())

v1x, v1y = x2 - x1, y2 - y1
v2x, v2y = -v1y, v1x

x3, y3 = x2 + v2x, y2 + v2y
x4, y4 = x3 - v1x, y3 - v1y

print(x3, y3, x4, y4)
