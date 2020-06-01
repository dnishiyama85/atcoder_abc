n = int(input())
v = list(map(int, input().strip().split()))

v = sorted(v, reverse=True)

while len(v) > 1:
    a = v.pop(-1)
    b = v.pop(-1)
    c = (a + b) / 2
    v.append(c)
    v = sorted(v, reverse=True)

last = v[0]
print(last)
