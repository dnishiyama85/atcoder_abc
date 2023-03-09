n = int(input())
as_ = list(map(int, input().strip().split()))

# 最大の偶数 + 2番めに大きい偶数
# 最大の奇数 + 2番めに大きい奇数
# 存在しないのは N=2 で奇数と偶数が一つずつあるときのみ

evens = sorted([a for a in as_ if a % 2 == 0])
odds = sorted([a for a in as_ if a % 2 == 1])

if len(evens) == 1 and len(odds) == 1:
    print(-1)
else:
    if len(evens) >= 2:
        max_e = evens[-1] + evens[-2]
    else:
        max_e = -1

    if len(odds) >= 2:
        max_o = odds[-1] + odds[-2]
    else:
        max_o = -1

    print(max(max_e, max_o))
