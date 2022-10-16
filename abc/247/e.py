n, x, y = map(int, input().strip().split())
as_ = list(map(int, input().strip().split()))

max_after = [0] * n
min_after = [0] * n

# L 以降の MAX
as_reversed = reversed(as_)
for i, a in enumerate(as_reversed):
    if i == 0:
        max_after[0] = as_[0]
        min_after[0] = as_[0]
    else:
        max_after[i] = max(a, max_after[i - 1])
        min_after[i] = min(a, min_after[i - 1])

max_after = list(reversed(max_after))
min_after = list(reversed(min_after))

now_max = as_[0]
now_min = as_[0]
total_count = 0

R = 0
for L in range(n):
    # L を動かしたことでの最大値最小値の更新
    if L > 0 and now_max == as_[L - 1]:
        now_max = max_after[L]
    if L > 0 and now_min == as_[L - 1]:
        now_min = min_after[L]

    while L <= R:
        if now_max == x and now_min == y:
            total_count += 1

        R += 1
        if R >= n:
            break
        # R を動かしたことでの最大値最小値の更新
        if now_max < as_[R]:
            now_max = as_[R]

        if now_min > as_[R]:
            now_min = as_[R]

print(total_count)
