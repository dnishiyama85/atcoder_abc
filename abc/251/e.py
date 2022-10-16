import sys
sys.setrecursionlimit(1000000)

n = int(input())
as_ = list(map(int, input().strip().split()))

# i 番目の行動を取る場合の費用の最小値を返す
def solve(i, do, do_first):
    if i == n:
        return 0

    if do:
        cost = as_[i]
        # 次の行動は取る場合と取らない場合の両方考えられる
        # ただし、 i == n - 1 のときは最初の行動に左右される。
        # 最初の行動をとっていない場合は n-1 の行動は取らざるを得ない。
        if i == n - 2 and not do_first:
            cost += solve(i + 1, True, do_first)
        else:
            # そうでないときは取る場合と取らない場合がある。
            c1 = solve(i + 1, True, do_first)
            c2 = solve(i + 1, False, do_first)
            cost += min(c1, c2)

        return cost
    else:
        # 次の行動は取らざるを得ない
        c = solve(i + 1, True, do_first)
        return c


c1 = solve(0, True, True)
c2 = solve(0, False, False)

print(min(c1, c2))
