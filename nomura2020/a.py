h1, m1, h2, m2, k = map(int, input().strip().split())

begin = h1 * 60 + m1
end = h2 * 60 + m2

last_start = end - k

ans = last_start - begin

print(ans)
