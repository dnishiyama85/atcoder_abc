import numpy as np

n = int(input())
data = []
for _ in range(n):
    a, b = list(map(int, input().strip().split()))
    data.append((a, b))

data = np.array(data)
# 火がぶつかる = 導火線がすべて燃える
# i本目が燃え終わるまでにかかる時間
times = data[:, 0] / data[:, 1]
cumsum_times = np.cumsum(times)

if n == 1:
    print(data[0, 0] / 2)
else:
    for i in range(n):
        # i 本目でぶつかるかどうか？
        t1 = cumsum_times[i]
        t2 = cumsum_times[-1] - (cumsum_times[i] if i > 0 else 0)
        # print(f"{i}: {t1}, {t2}")
        if t1 >= t2:
            # ぶつかる
            break

    # print(f"{i}本目でぶつかる")
    # i本目の左端が燃え始めるまでの時間
    tL = cumsum_times[i - 1]
    # print("tL =", tL)

    # i本目の右端が燃え始めるまでの時間
    tR = cumsum_times[-1] - cumsum_times[i]
    # print("tR =", tR)

    if tL > tR:
        # 右端はもう燃えている。その位置は
        pR = data[i][0] - (tL - tR) * data[i][1]
        # ぶつかる位置は
        ans = pR / 2 + np.sum(data[:i, 0])
    else:
        # 左端はもう燃えている。その位置は
        pL = (tR - tL) * data[i][1]
        # print("pL =", pL)
        # ぶつかる位置は
        ans = (data[i][0] - pL) / 2 + pL + np.sum(data[:i, 0])

    print(ans)

