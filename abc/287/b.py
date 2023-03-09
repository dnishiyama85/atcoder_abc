n, m = map(int, input().strip().split())
ss = []
ts = []

for _ in range(n):
    s = input().strip()
    s = s[3:]
    ss.append(s)

for _ in range(m):
    t = input().strip()
    ts.append(t)


count = 0
for s in ss:
    for t in ts:
        if s == t:
            count += 1
            break

print(count)
