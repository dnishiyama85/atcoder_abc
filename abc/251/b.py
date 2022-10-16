n, w = map(int, input().strip().split())
as_ = list(map(int, input().strip().split()))

ans = set()

# 1個選ぶ
for a in as_:
    if a <= w:
        ans.add(a)

# 2個選ぶ
for i, a1 in enumerate(as_):
    for j, a2 in enumerate(as_):
        if i == j:
            continue

        if a1 + a2 <= w:
            ans.add(a1 + a2)

# 3個選ぶ
for i, a1 in enumerate(as_):
    for j, a2 in enumerate(as_):
        for k, a3 in enumerate(as_):
            if i == j or j == k or k == i:
                continue

            if a1 + a2 + a3 <= w:
                ans.add(a1 + a2 + a3)

print(len(ans))
