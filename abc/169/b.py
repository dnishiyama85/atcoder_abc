n = int(input())
as_ = sorted(list(map(int, input().strip().split())))

ans = 1
if as_[0] == 0:
    print(0)
    exit(0)

for a in as_:
    ans *= a
    if ans > 1e18:
        print(-1)
        exit(0)

print(ans)
