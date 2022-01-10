import math

a, b, x = map(int, input().strip().split())

vol = a * a * b
if vol <= 2 * x:
    theta = math.atan(2 * (vol - x) / a**3)
else:
    theta = math.atan(a * b**2 / (2 * x))

print(theta * 360 / (2 * math.pi))
