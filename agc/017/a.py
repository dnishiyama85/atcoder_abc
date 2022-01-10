# from scipy.special import comb
from scipy.misc import comb

n, p = map(int, input().strip().split())
as_ = list(map(int, input().strip().split()))

num_evens = len([a for a in as_ if a % 2 == 0])
num_odds = len([a for a in as_ if a % 2 == 1])

counts = 0
if p == 0:
    # 全部で偶数枚食べる = 偶数枚の袋 a 個 + 奇数枚の袋 b = 2k 個
    # 0袋食べる場合も OK.
    counts += 1
    # 1袋以上食べる場合
    for i in range(1, n + 1):
        # 全部で i 袋食べるとする i = 1 〜 n
        for a in range(i + 1):
            # そのうち偶数枚の袋を a 個食べる方法
            even_ways = comb(num_evens, a, exact=True)
            # 奇数枚の袋は (i - a) 個食べるが、それは偶数でなければならない
            b = (i - a)
            if b % 2 == 1 or b < 0:
                continue
            else:
                odd_ways = comb(num_odds, b, exact=True)

            counts += even_ways * odd_ways

else:
    # 全部で奇数枚食べる = 偶数枚の袋 a 個 + 奇数枚の袋 b = 2k + 1個 (k >= 0)
    # 奇数の袋は0ではいけない (k >= 0)
    # 0袋食べるのはダメ
    # 1袋以上食べる場合
    for i in range(1, n + 1):
        # 全部で i 袋食べるとする
        for b in range(0, i + 1):
            # 奇数枚の袋を b = 2k + 1 個食べる
            if b % 2 == 0:
                continue
            # すると偶数枚の袋は a = i - b 個食べる
            a = i - b
            if a < 0:
                continue

            odd_ways = comb(num_odds, b, exact=True)
            even_ways = comb(num_evens, a, exact=True)
            counts += even_ways * odd_ways

print(counts)
