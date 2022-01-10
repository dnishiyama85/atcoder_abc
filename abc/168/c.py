import math

A, B, H, M = map(int, input().strip().split())

minutes = 60 * H + M

angle_long = minutes / 60 * 2 * math.pi
angle_short = minutes / (12 * 60) * 2 * math.pi

x_long = A * math.cos(angle_long)
y_long = A * math.sin(angle_long)

x_short = B * math.cos(angle_short)
y_short = B * math.sin(angle_short)

dist = math.sqrt((x_long - x_short)**2 + (y_long - y_short)**2)

print(dist)
