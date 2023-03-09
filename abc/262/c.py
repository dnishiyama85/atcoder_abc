n = int(input())
as_ = list(map(int, input().strip().split()))

# 0-index にする
for i in range(n):
    as_[i] = as_[i] - 1

# min(ai, aj) = i
# max(ai, aj) = j
# が成り立つのは
# ai = i かつ aj = j のとき
# または
# aj = i かつ ai = j のとき。

# 前者が成り立つのは
# ak = k なる k の個数を N として N (N - 1) / 2 である。

# 後者が成り立つのは、
# i を一つ固定したときに、j = ai と決まるので、
# aj == i が成り立っているかを見て
# 成り立っていれば +1 カウントすれば良い。

# 前者
same = 0
for k in range(n):
    if as_[k] == k:
        same += 1

ans = same * (same - 1) // 2

# 後者
for i in range(n):
    j = as_[i]
    if as_[j] == i and i < j:
        ans += 1

print(ans)
