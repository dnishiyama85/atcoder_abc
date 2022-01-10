import bisect

n, q = list(map(int, input().strip().split()))
as_ = sorted(list(map(int, input().strip().split())))

for _ in range(q):
    x = int(input())
    idx = bisect.bisect_left(as_, x)
    ans = n - idx
    print(ans)
