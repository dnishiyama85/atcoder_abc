n = int(input())
hs = list(map(int, input().strip().split()))
now = hs[0]

for h in hs[1:]:
    if now < h:
        now = h
    else:
        break

print(now)
