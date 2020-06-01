n = int(input())
as_ = list(map(int, input().strip().split()))

current_idx = -1
next_num = 1
broken = 0
success = False

while broken < n:
    # current_idx より右で next_num が見つかるまで探す
    found = False
    for idx in range(current_idx + 1, n):
        if as_[idx] == next_num:
            # 見つかった
            current_idx = idx
            next_num += 1
            found = True
        else:
            broken += 1

    if n - broken == next_num - 1:
        success = True
        break

if n - broken > 0 and success:
    print(broken)
else:
    print(-1)
