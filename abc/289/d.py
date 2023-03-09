n = int(input())
as_ = list(map(int, input().strip().split()))
m = int(input())
bs = list(map(int, input().strip().split()))
x = int(input())

# 0: 未確定, 1: OK, 2: OK だけどモチに捕まっている
dp = [0] * (x + 1)
dp[0] = 1

bs = set(bs)

# i段目に登ることができるかどうかの DP
for i in range(1, x + 1):
    for a in as_:
        if i - a < 0:
            continue
        elif dp[i - a] == 1:
            # たどり着いたが、モチに捕まるかどうか
            dp[i] = 2 if i in bs else 1

if dp[x] == 1 or dp[x] == 2:
    print('Yes')
else:
    print('No')
