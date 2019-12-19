n = int(input())
s = input().strip()

cumsum = [0] * n

# 西を向いている人数の累積和
for i in range(n):
    dir = s[i]
    prev = cumsum[i - 1] if i > 0 else 0
    cur = 1 if dir == 'W' else 0
    cumsum[i] = prev + cur


num_min = 1000000


for i in range(n):
    # i 番目の人がリーダーになる場合
    # リーダーより西の人で向きを変える人の数
    # = i番目より前で西を向いている人数
    w = cumsum[i - 1] if i > 0 else 0
    # リーダーより東の人で向きを変える人の数
    # = i番目より後で東を向いている人数
    e = n - (i + 1) - (cumsum[-1] - cumsum[i])

    num_min = min(num_min, w + e)

print(num_min)
