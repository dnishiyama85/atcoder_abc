n, x = map(int, input().strip().split())
as_ = map(int, input().strip().split())
as_ = sorted(as_)

cnt = 0
for a in as_:
    if x >= a:
        x -= a
        cnt += 1
    else:
        x = 0
        break

if x > 0 and cnt > 0:
    cnt -= 1

print(cnt)
