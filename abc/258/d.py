import numpy as np
n, x = map(int, input().strip().split())
as_ = []
bs = []
for _ in range(n):
    a, b = map(int, input().strip().split())
    as_.append(a)
    bs.append(b)

# ステージをi番目までクリアするときに最小の時間を更新する可能性があるのは
# = 1〜i まで映像を見て、残りのプレイをすべてiで行うとき。

min_time = 1e100

cumsum_a = np.cumsum(as_)
cumsum_b = np.cumsum(bs)
for i in range(n):
    time = 0
    if i >= x:
        break
    # i まで映像+プレイ
    time += cumsum_a[i] + cumsum_b[i]
    # 残り回数をすべてiでプレイ
    time += bs[i] * (x - (i + 1))
    if time < min_time:
        min_time = time

print(min_time)
