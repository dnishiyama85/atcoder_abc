r1, c1 = map(int, input().strip().split())
r2, c2 = map(int, input().strip().split())

r, c = r2 - r1, c2 - c1

if r < 0:
    r = -r

if c < 0:
    c = -c

if r < c:
    r, c = c, r

if r == 0 and c == 0:
    ans = 0
elif r == c:
    ans = 1
elif r - c <= 3:
    if c <= 1:
        ans = 1
    else:
        ans = 2
elif (r + c) % 2 == 0:
    ans = 2
elif r + c <= 6:
    ans = 2
else:
    ans = 3

print(ans)
