import math

r, x, y = map(int, input().strip().split())

d = math.sqrt(x**2 + y**2)

if r ** 2 > x ** 2 + y ** 2:
    ans = 2
elif (x**2 + y**2) % r**2 == 0:
    ans = math.ceil(math.sqrt((x**2 + y**2) / r**2))
else:
    ans = math.ceil(d / r)

print(ans)
